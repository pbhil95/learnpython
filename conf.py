# -*- coding: utf-8 -*-
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = ''
copyright = '2020,NVS'
author = 'Pankaj Bhilingwal'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

html_title = 'Home'

html_show_sphinx = False

html_add_permalinks = ""
# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_theme_path = os.path.join(BASE_DIR, 'learnpython')
#html_theme_path = [os.path.join(BASE_DIR, 'learnpython')]
html_theme = 'cloud'

html_css_files = ['css/my.css', 'css/hacks.css', 'css/basic.css']
latex_elements = {
    'inputenc': '',
    'utf8extra': '',
    'preamble': '''

\usepackage{fontspec}
\setsansfont{Arial}
\setromanfont{Arial}
\setmonofont{DejaVu Sans Mono}
''',
}


latex_engine = 'xelatex'