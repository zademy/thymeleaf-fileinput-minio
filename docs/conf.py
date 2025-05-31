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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/en/**', '**/es/**']

# Configuración de internacionalización (i18n)
language = 'es'  # Idioma por defecto
locale_dirs = ['locales/']  # Directorio donde se guardarán las traducciones
gettext_compact = False  # Genera archivos .po separados por documento
locale_purge = True  # Elimina archivos obsoletos al actualizar

translations = [
    ('es', 'Español'),
    ('en', 'English'),
    # Añade más idiomas según sea necesario
]

# Configuración de metadatos para cada idioma
all_ = {}
for code, name in translations:
    if code == 'es':
        all_[code] = {
            'version': release,
            'language': 'es',
            'og:locale': 'es_MX',
            'og:description': 'Documentación de Thymeleaf FileInput con integración MinIO',
        }
    elif code == 'en':
        all_[code] = {
            'version': release,
            'language': 'en',
            'og:locale': 'en_US',
            'og:description': 'Thymeleaf FileInput with MinIO integration documentation',
        }

# Configuración de extensiones
extensions = [
    # Extensiones estándar de Sphinx
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',  # Para referencias automáticas a secciones
    'sphinx.ext.todo',  # Soporte para listas de tareas
    'sphinx.ext.coverage',  # Verificación de cobertura de documentación
    'sphinx.ext.ifconfig',  # Directivas condicionales
    'sphinx.ext.imgconverter',  # Conversión de imágenes
    'sphinx.ext.graphviz',  # Soporte para gráficos Graphviz
    'sphinx.ext.extlinks',  # Enlaces externos abreviados
    'sphinx.ext.mathjax',  # Soporte para fórmulas matemáticas
    'sphinx_intl',  # Soporte para internacionalización
    
    # Extensiones de terceros
    'sphinx_rtd_theme',  # Tema Read the Docs
    'myst_parser',  # Soporte para Markdown
    'sphinx_copybutton',  # Botón de copia en bloques de código
    'sphinxcontrib.mermaid',  # Diagramas Mermaid
    'sphinxcontrib.httpdomain',  # Documentación de APIs REST
    'sphinxext.opengraph',  # Mejora para compartir en redes sociales
]

# Configuración para httpdomain
http_index_shortname = 'api'
http_index_localname = 'API Reference'
http_index_ignore_prefixes = ['/_']
http_index_ignore_resources = False

# Configuración para autosectionlabel
autosectionlabel_prefix_document = True  # Incluye el nombre del documento en la referencia
autosectionlabel_maxdepth = 3  # Nivel máximo de anidación para crear etiquetas automáticas

# Configuración para las extensiones

# -- Opciones para sphinx.ext.todo --
todo_include_todos = True  # Mostrar tareas pendientes
todo_emit_warnings = True  # Mostrar advertencias para tareas pendientes

# -- Opciones para sphinx.ext.coverage --
coverage_show_missing_items = True  # Mostrar elementos sin documentar
coverage_write_headline = False  # No escribir encabezado en el informe

# -- Opciones para sphinx.ext.graphviz --
graphviz_output_format = 'svg'  # Usar SVG para gráficos (mejor calidad)
graphviz_dot_args = ['-Gfontname=DejaVu Sans',  # Fuente para los gráficos
                     '-Nfontname=DejaVu Sans',
                     '-Efontname=DejaVu Sans']

# -- Opciones para sphinx.ext.extlinks --
extlinks = {
    'issue': ('https://github.com/zademy/thymeleaf-fileinput-minio/issues/%s', 'issue %s'),
    'pull': ('https://github.com/zademy/thymeleaf-fileinput-minio/pull/%s', 'PR %s'),
}

# -- Opciones para sphinx.ext.mathjax --
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
    },
}

# Configuración de Mermaid
mermaid_output_format = 'raw'  # Usa SVG/PNG para PDF, raw para HTML
mermaid_d3_zoom = False  # Desactivar zoom por defecto


# Configuración del tema
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'  # Asegúrate de tener un logo en _static/logo.png
html_favicon = '_static/favicon.ico'  # Añade un favicon si lo tienes


# Evitar problemas de caché añadiendo un timestamp a los archivos estáticos
import time
html_last_updated_fmt = '%Y-%m-%d %H:%M:%S'

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
rtd_version = 'latest'  # or 'stable' for the stable version
rtd_project = 'thymeleaf-fileinput-minio'  # Your ReadTheDocs project name
rtd_language = 'es'  # The language of your documentation

# Configuración unificada para html_context
html_context = {
    # Información de GitHub
    'display_github': True,
    'github_user': 'zademy',
    'github_repo': 'thymeleaf-fileinput-minio',
    'github_version': 'main',
    'conf_py_path': '/docs/',
    
    # Configuración de internacionalización
    'languages': translations,
    'current_language': language,
    'current_version': release,
    'version': release,
    'language': language,
    'languages_dict': {code: name for code, name in translations},
    'translations': translations,
    'default_lang': 'es',
    'LANGUAGES': translations,
    
    # ReadTheDocs specific variables
    'build_id': str(int(time.time())),
    'rtd_version': rtd_version,
    'rtd_project': rtd_project,
    'rtd_url': f'https://{rtd_project}.readthedocs.io/{rtd_language}/{rtd_version}'
}
