# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Thymeleaf FileInput with MinIO'
copyright = '2025, Zademy'
author = 'Zademy'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinxcontrib.mermaid',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

import sys
sys.setrecursionlimit(1_500)

# Configuración de templates
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'es'

# Configuración de extensiones
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinxcontrib.mermaid',
    'myst_parser',
]

# Configuración de Mermaid
mermaid_version = '11'  # Usar Mermaid v11
mermaid_output_format = 'svg'  # Usar SVG para mejor calidad

# Configuración del tema
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuración básica de JavaScript
html_js_files = [
    'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js',
]

def setup(app):
    # Configuración de Mermaid
    app.add_js_file(f'https://cdn.jsdelivr.net/npm/mermaid@{mermaid_version}/dist/mermaid.min.js')
    
    # Configuración básica de Mermaid
    app.add_js_file(None, 
                   body="""
                   document.addEventListener('DOMContentLoaded', function() {
                       if (typeof mermaid !== 'undefined') {
                           mermaid.initialize({
                               startOnLoad: true,
                               theme: 'default',
                               securityLevel: 'loose',
                               fontFamily: 'Arial, sans-serif'
                           });
                       }
                   });
                   """,
                   priority=200)

# Configuración de archivos estáticos
html_static_path = ['_static']

# Configuración del tema
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# Configuración para archivos estáticos
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# Evitar problemas de caché añadiendo un timestamp a los archivos estáticos
import time
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'
html_context = {
    'build_id': str(int(time.time())),
}

def setup(app):
    # Cargar Mermaid
    app.add_js_file(f'https://cdn.jsdelivr.net/npm/mermaid@{mermaid_version}/dist/mermaid.min.js')
    
    # Inicialización básica de Mermaid
    app.add_js_file(None, 
                   body="""
                   document.addEventListener('DOMContentLoaded', function() {
                       if (typeof mermaid !== 'undefined') {
                           mermaid.initialize({
                               startOnLoad: true,
                               theme: 'default',
                               securityLevel: 'loose',
                               fontFamily: 'Arial, sans-serif'
                           });
                       }
                   });
                   """,
                   priority=200)
    
    # Asegurarse de que el directorio _static existe
    import os
    os.makedirs('_static', exist_ok=True)

# -- Options for autodoc -----------------------------------------------------
# Mock dependencies that might not be available during documentation build
autodoc_mock_imports = [
    'org.springframework',
    'lombok',
    'jakarta',
    'io.minio',
    'java',
    'javax',
]

# -- Options for ReadTheDocs -------------------------------------------------
html_show_sourcelink = False
html_show_sphinx = False
