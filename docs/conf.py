"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup ----------------------------------------------------------------

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -------------------------------------------------------

project = "sphinxcontrib-video"
author = "Raphael Massabot"
copyright = f"2018-{datetime.now().year}, {author}"
release = "0.2.1"

# -- General configuration -----------------------------------------------------

extensions = ["sphinxcontrib.video", "sphinx_design"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ---------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_context = {
    "github_user": "sphinx-contrib",
    "github_repo": "video",
    "github_version": "master",
    "doc_path": "docs",
}
html_theme_options = {
    "logo": {"text": project},
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sphinx-contrib/video",
            "icon": "fa-brands fa-github",
        }
    ],
}
