# Sphinx configuration for Metabarcoding 101
project = "Metabarcoding 101"
author = "Till-Hendrik Macher"
copyright = "2026, Till-Hendrik Macher"

extensions = [
    "myst_parser",        # write pages in Markdown
    "sphinx_copybutton",  # copy button on code blocks
]

myst_enable_extensions = [
    "colon_fence",  # ::: note blocks
    "deflist",
]
myst_heading_anchors = 3

source_suffix = {".md": "markdown"}
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_title = "Metabarcoding 101"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
}

# Shows an "Edit on GitHub" link on every page
html_context = {
    "display_github": True,
    "github_user": "YOUR-GITHUB-USERNAME",
    "github_repo": "metabarcoding101",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
