# Configuration file for the Sphinx documentation builder.
from datetime import datetime
now = datetime.now()
this_year = now.year
# -- Project information

project = 'Nuclear Electronic Experiment Handbook'
copyright = f'2024-{this_year}, 复旦大学'
author = '复旦大学'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for Search
html_search_enable = True

html_search_options = {
    'type': 'default',
    'lang': ['en', 'zh'],
}
