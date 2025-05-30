# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Importar el tema Bootstrap
import sphinx_bootstrap_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thymeleaf FileInput with MinIO'
copyright = '2025, Zademy'
author = 'Zademy'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinxcontrib.jquery',  # Añadido explícitamente para resolver problemas con jQuery
    # No es necesario añadir sphinx_bootstrap_theme como extensión si solo se usa como tema
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Configuración del tema Bootstrap
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Opciones del tema Bootstrap
html_theme_options = {
    'navbar_title': "Thymeleaf FileInput with MinIO",
    'bootswatch_theme': "united",  # Tema de Bootswatch (ej. "flatly", "cerulean", "cosmo", etc.)
    'navbar_sidebarrel': True,
    'navbar_links': [
        ("Inicio", "index", True),
        ("Configuración", "configuration", True),
        ("Uso", "usage", True),
        ("Comenzar", "getting-started", True),
    ],
    'navbar_pagenav': True,
    'navbar_pagenav_name': "En esta página",
    'globaltoc_depth': 2,
    'globaltoc_includehidden': False,
    'source_link_position': None,
    'bootstrap_version': "3",
}

html_static_path = ['_static']

# -- Options for autodoc -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

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
# https://docs.readthedocs.io/en/stable/config-file/v2.html

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer.
html_show_sphinx = False
