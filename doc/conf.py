#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, shlex

sys.path.insert(0, os.path.abspath(".."))

extensions = [
    "sphinx.ext.autodoc",
]

source_suffix = ".rst"
master_doc = "index"

project = "pyVDK"
copyright = "2015, Gabriel Cavallo"
author = "Gabriel Cavallo"

version = "0.1"
release = "0.1"

language = None
exclude_patterns = ["_build"]
pygments_style = "sphinx"
todo_include_todos = False

html_theme = "alabaster"
html_theme_options = {
	"nosidebar": "true",
	"github_user": "gcavallo",
	"github_repo": "pyVDK",
	"github_banner": "true",
	"show_powered_by": "false"
}
html_title = "pyVDK"
html_show_sphinx = False
html_show_copyright = True
htmlhelp_basename = "pyVDKdoc"

man_pages = [
    (master_doc, "pyvdk", "pyVDK Documentation",
     [author], 1)
]
