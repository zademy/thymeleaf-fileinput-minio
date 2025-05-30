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

# Configuración para Mermaid
mermaid_version = '10.9.0'  # Última versión estable

# Configuración global de Mermaid
mermaid_params = {
    'theme': 'default',
    'startOnLoad': 'true',
    'securityLevel': 'loose',
    'fontFamily': '"Arial", sans-serif',
    'themeCSS': '.label { font-family: Arial; }',
    'themeVariables': {
        'primaryColor': '#f0f0f0',
        'primaryTextColor': '#333',
        'primaryBorderColor': '#666',
        'lineColor': '#333',
        'secondaryColor': '#f0f0f0',
        'tertiaryColor': '#f0f0f0'
    },
    'gantt': {
        'barHeight': 20,
        'fontSize': 12
    },
    'flowchart': {
        'useMaxWidth': True,
        'htmlLabels': True
    }
}

# Incluir Mermaid desde CDN con SRI para seguridad
html_js_files = [
    {
        'src': f'https://cdn.jsdelivr.net/npm/mermaid@{mermaid_version}/dist/mermaid.min.js',
        'integrity': 'sha384-...',  # Agregar SRI hash si es necesario
        'crossorigin': 'anonymous'
    }
]

# -- Options for HTML output -------------------------------------------------
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
