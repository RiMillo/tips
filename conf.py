# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tips'
copyright = '2025, Riccardo Milani'
author = 'RiMillo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# master_doc = "README"

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', 'how-to-pdf.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# MyST parser config
myst_heading_anchors = 5

# LaTeX config
latex_elements = {
    "preamble": r"""
\usepackage{xcolor}
\definecolor{BlueX}{RGB}{0,62,92}
\xdefinecolor{lGreenRT}{RGB}{0,180,110}
""",
    "maketitle": r"""
\begin{center}
\bfseries \scshape \Huge \color{BlueX}%
Tips \& stuff
\end{center}
""",
    "extraclassoptions": "openany",
    "sphinxsetup": r"""
    TitleColor={RGB}{0,62,92},
    InnerLinkColor={RGB}{0,180,110},
    OuterLinkColor={RGB}{0,180,110},
    VerbatimColor={gray}{0.95},
    VerbatimBorderColor={RGB}{0,62,92},
    VerbatimHighlightColor={RGB}{0,62,92},
    """,
    "papersize": "a4paper",
}
