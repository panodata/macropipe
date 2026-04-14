# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# ruff: noqa: ERA001

project = "macropipe"
copyright = "2024-2026, The Panodata Developers."  # noqa: A001
author = "The Panodata Developers"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.autodoc",
    # "sphinx.ext.autodoc.typehints",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinxcontrib.mermaid",
    "sphinxext.opengraph",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "readme.md"]
suppress_warnings = ["myst.strikethrough"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinxawesome_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_title = "Macropipe"

html_theme_options = {
    "extra_header_link_icons": {
        "repository on GitHub": {
            "link": "https://github.com/panodata/macropipe",
            "icon": (
                '<svg height="16px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" '
                'fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                "14.853 20.608 1.087.2 1.483-.47 1.483-1.047 "
                "0-.516-.019-1.881-.03-3.693-6.04 "
                "1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 "  # noqa
                "2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 "
                "1.803.197-1.403.759-2.36 "
                "1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 "
                "0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 "
                "1.822-.584 5.972 2.226 "
                "1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 "
                "4.147-2.81 5.967-2.226 "
                "5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 "
                "2.232 5.828 0 "
                "8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 "
                "2.904-.027 5.247-.027 "
                "5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 "
                '22.647c0-11.996-9.726-21.72-21.722-21.72" '
                'fill="currentColor"/></svg>'
            ),
        },
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_show_sourcelink = True


# -- Intersphinx ----------------------------------------------------------

intersphinx_mapping = {
    "tikray": ("https://tikray.readthedocs.io/", None),
}
linkcheck_ignore = []

# Disable caching remote inventories completely.
# http://www.sphinx-doc.org/en/stable/ext/intersphinx.html#confval-intersphinx_cache_limit
# intersphinx_cache_limit = 0


# -- Extension configuration -------------------------------------------------

sphinx_tabs_valid_builders = ["linkcheck"]
todo_include_todos = True

# Configure sphinx-copybutton
copybutton_remove_prompts = True
copybutton_line_continuation_character = "\\"
copybutton_prompt_text = (
    r">>> |\.\.\. |\$ |sh\$ |PS> |cr> |mysql> |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: |expression: "
)
copybutton_prompt_is_regexp = True

# Configure sphinxext-opengraph
ogp_site_url = "https://macropipe.readthedocs.io/"
ogp_enable_meta_description = True
# ogp_image = "http://example.org/image.png"
# ogp_description_length = 300

# Configure sphinx-sitemap
sitemap_url_scheme = "{link}"
sitemap_excludes = [
    "search.html",
    "genindex.html",
    "_snippet/*",
]

# Configure AutoAPI
autoapi_dirs = ["../src"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
# autodoc_typehints = 'description'

# -- Options for MyST -------------------------------------------------

myst_heading_anchors = 3
myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_substitutions = {}
