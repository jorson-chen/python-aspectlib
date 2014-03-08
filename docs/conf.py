# -*- coding: utf-8 -*-
import re
import os
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'
master_doc = 'index'
project = u'python-aspectlib'
copyright = u'2014, Ionel Cristian Mărieș'
version = release = re.findall(
    'version="(.*)"',
    open(os.path.join(os.path.dirname(__file__), '../setup.py')).read()
)[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

pygments_style = 'trac'
html_theme = 'traditional'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

htmlhelp_basename = 'python-aspectlib-docs'
