# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import subprocess
import sys
import mock
from mock import MagicMock
from unittest.mock import MagicMock


for mod in ['maya.cmds', 'pymel.core']: 
    sys.modules[mod] = mock.MagicMock()
#sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, '/root/ros_ws/src/assignment_1')
#sys.path.insert(0, os.path.abspath('../..'))

subprocess.call('doxygen Doxyfile.in', shell=True)

# -- Project information -----------------------------------------------------

project = 'Adaptive Autonomous Surveillance Robot for Indoor Environments with Energy Management'
copyright = '2023, Ankur Kohli'
author = 'Ankur Kohli'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    "sphinx.ext.napoleon",
    'sphinx.ext.inheritance_diagram',
    'breathe'
]
#autodoc_mock_imports = ["scripts.finite_statemachine", "scripts.robot_states", "scripts.load_environment", "scripts.helper"]



class MockModule(MagicMock):
    __all__ = []

MOCK_MODULES = [
    'scripts.finite_statemachine',
    'scripts.robot_states',
    'scripts.load_environment',
    'scripts.helper',
]

sys.modules.update((mod_name, MockModule()) for mod_name in MOCK_MODULES)

# Add this line to include functions in the mock (replace 'function_name' with the actual function names)
autodoc_mock_functions = ["scripts.finite_statemachine.*", "scripts.robot_states.*", "scripts.load_environment.*", "scripts.helper.*"]



# Exclude mocked modules from autodoc
def skip_mocked_members(app, what, name, obj, skip, options):
    if name in MOCK_MODULES:
        return True
    return None

def setup(app):
    app.connect("autodoc-skip-member", skip_mocked_members)


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

highlight_language = 'c++'
source_suffix = '.rst'
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# -- Options for intersphinx extension ---------------------------------------
# Example configuration for intersphinx: refer to the Python standard library. 
#intersphinx_mapping = {'https://docs.python.org/': None}
intersphinx_mapping = {'python': ('https://docs.python.org/', None)}
# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing. 
todo_include_todos = True
# -- Options for breathe
breathe_projects = {
"Adaptive_Autonomous_Surveillance_Robot_for_Indoor_Environments_with_Energy_Management": "_build/xml/"
}
breathe_default_project = "Adaptive_Autonomous_Surveillance_Robot_for_Indoor_Environments_with_Energy_Managemen"
breathe_default_members = ('members', 'undoc-members')
