#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para manejar traducciones en la documentación de Sphinx.

Uso:
    python i18n.py extract    # Extraer cadenas a traducir
    python i18n.py update     # Actualizar archivos .po
    python i18n.py compile    # Compilar traducciones
    python i18n.py all        # Ejecutar todos los pasos
"""
import os
import sys
import subprocess
from pathlib import Path

# Configuración
BASE_DIR = Path(__file__).parent
LOCALE_DIR = BASE_DIR / 'locales'
SOURCE_DIR = BASE_DIR / 'source'
BUILD_DIR = BASE_DIR / 'build'
LANGUAGES = ['es', 'en']  # Añade más idiomas según sea necesario

def run_command(command, cwd=None):
    """Ejecuta un comando en la terminal."""
    print(f"\nEjecutando: {' '.join(command)}\n")
    result = subprocess.run(
        command,
        cwd=cwd or BASE_DIR,
        check=True,
        text=True,
        capture_output=True
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def extract_messages():
    """Extrae las cadenas traducibles a archivos .pot."""
    print("\n=== Extrayendo cadenas a traducir ===\n")
    
    # Crear directorios necesarios
    (LOCALE_DIR / 'en' / 'LC_MESSAGES').mkdir(parents=True, exist_ok=True)
    
    # Extraer mensajes
    run_command([
        'sphinx-build',
        '-b', 'gettext',
        '-d', str(BUILD_DIR / 'doctree'),
        str(SOURCE_DIR),
        str(LOCALE_DIR / 'pot')
    ])
    
    # Crear archivos .po iniciales si no existen
    for lang in LANGUAGES:
        if lang == 'es':
            continue  # Saltar el idioma fuente
            
        lang_dir = LOCALE_DIR / lang / 'LC_MESSAGES'
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        for pot_file in (LOCALE_DIR / 'pot').glob('*.pot'):
            po_file = lang_dir / f"{pot_file.stem}.po"
            if not po_file.exists():
                run_command([
                    'sphinx-intl', 'init',
                    '-l', lang,
                    '-i', str(pot_file.relative_to(BASE_DIR)),
                    '-d', str(LOCALE_DIR.relative_to(BASE_DIR))
                ])
    
    print("\n=== Cadenas extraídas correctamente ===\n")

def update_translations():
    """Actualiza los archivos .po con las nuevas cadenas."""
    print("\n=== Actualizando traducciones ===\n")
    
    run_command([
        'sphinx-intl', 'update',
        '-p', str(LOCALE_DIR / 'pot'),
        '-d', str(LOCALE_DIR),
        '--language', ','.join([lang for lang in LANGUAGES if lang != 'es'])
    ])
    
    print("\n=== Traducciones actualizadas ===\n")

def compile_translations():
    """Compila las traducciones a archivos .mo."""
    print("\n=== Compilando traducciones ===\n")
    
    for lang in LANGUAGES:
        if lang == 'es':
            continue  # Saltar el idioma fuente
            
        run_command([
            'sphinx-intl', 'compile',
            '-d', str(LOCALE_DIR),
            '--language', lang
        ])
    
    print("\n=== Traducciones compiladas correctamente ===\n")

def build_docs():
    """Construye la documentación para todos los idiomas."""
    print("\n=== Construyendo documentación ===\n")
    
    for lang in LANGUAGES:
        print(f"\n=== Construyendo para idioma: {lang} ===\n")
        run_command([
            'sphinx-build',
            '-b', 'html',
            '-D', f'language={lang}',
            '-d', str(BUILD_DIR / 'doctree' / lang),
            str(SOURCE_DIR),
            str(BUILD_DIR / 'html' / lang)
        ])
    
    print("\n=== Documentación construida correctamente ===\n")

def main():
    """Función principal."""
    if len(sys.argv) < 2:
        print("Uso: python i18n.py [extract|update|compile|build|all]")
        return 1
    
    command = sys.argv[1].lower()
    
    try:
        if command == 'extract':
            extract_messages()
        elif command == 'update':
            update_translations()
        elif command == 'compile':
            compile_translations()
        elif command == 'build':
            build_docs()
        elif command == 'all':
            extract_messages()
            update_translations()
            compile_translations()
            build_docs()
        else:
            print(f"Comando no reconocido: {command}")
            return 1
    except subprocess.CalledProcessError as e:
        print(f"\nError al ejecutar el comando: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
