# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Thymeleaf FileInput with MinIO'
copyright = '2025, Zademy'
author = 'Zademy'
release = '1.0.0'

# OpenGraph metadata
ogp_site_url = 'https://thymeleaf-fileinput-minio.readthedocs.io/'
ogp_site_name = project
ogp_image = 'https://thymeleaf-fileinput-minio.readthedocs.io/en/latest/_static/logo.png'
ogp_description = 'Documentación de Thymeleaf FileInput con integración MinIO'
ogp_type = 'website'
ogp_enable_meta_description = True

# Opcional: Configuración adicional de OpenGraph
ogp_custom_meta_tags = [
    '<meta property="twitter:card" content="summary_large_image" />',
    '<meta property="twitter:site" content="@zademy_tech" />',
    '<meta name="theme-color" content="#4c1d95" />',
]

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
    'myst_parser',
    'sphinx_copybutton',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',  # Para referencias automáticas a secciones
    'sphinxcontrib.mermaid',
    'sphinxcontrib.httpdomain',  # Para documentación de APIs REST
    'sphinxext.opengraph',  # Para mejorar el compartido en redes sociales
]

# Configuración para httpdomain
http_index_shortname = 'api'
http_index_localname = 'API Reference'
http_index_ignore_prefixes = ['/_']
http_index_ignore_resources = False

# Configuración para autosectionlabel
autosectionlabel_prefix_document = True  # Incluye el nombre del documento en la referencia
autosectionlabel_maxdepth = 3  # Nivel máximo de anidación para crear etiquetas automáticas

# Configuración de Mermaid
mermaid_output_format = 'raw'  # Usa SVG/PNG para PDF, raw para HTML
mermaid_d3_zoom = False  # Desactivar zoom por defecto
mermaid_init_js = """
    mermaid.initialize({
        startOnLoad: true,
        theme: 'default',
        securityLevel: 'loose',
        fontFamily: 'Arial, sans-serif',
        logLevel: 'fatal'
    });
"""

# Configuración del tema
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'  # Asegúrate de tener un logo en _static/logo.png
html_favicon = '_static/favicon.ico'  # Añade un favicon si lo tienes


# Evitar problemas de caché añadiendo un timestamp a los archivos estáticos
import time
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'
html_context = {
    'build_id': str(int(time.time())),
}

# Configuración de Mermaid
mermaid_version = '11.2.0'  # Última versión estable


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

# -- Status Badges Configuration --------------------------------------------
# These variables are used to generate the status badges in the documentation
# You can customize the branch name if needed
rtd_version = 'latest'  # or 'stable' for the stable version
rtd_project = 'thymeleaf-fileinput-minio'  # Your ReadTheDocs project name
rtd_language = 'es'  # The language of your documentation

# Add the status badges to the HTML context
html_context = {
    'build_id': str(int(time.time())),
    'display_github': True,  # Enable 'Edit on GitHub' link
    'github_user': 'zademy',  # Your GitHub username/organization
    'github_repo': 'thymeleaf-fileinput-minio',  # Your repository name
    'github_version': 'main',  # Your default branch
    'conf_py_path': '/docs/',  # Path from the root of the project to the docs
    
    # ReadTheDocs specific variables for badges
    'rtd_version': rtd_version,
    'rtd_project': rtd_project,
    'rtd_url': f'https://{rtd_project}.readthedocs.io/{rtd_language}/{rtd_version}'
}
