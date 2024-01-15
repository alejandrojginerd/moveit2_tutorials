# -*- coding: utf-8 -*-
#
# rosindex documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  2 16:34:57 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with auexamplesc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import itertools
import os
import sys
import time

from docutils.parsers.rst import Directive

sys.path.append(os.path.abspath("./sphinx-multiversion"))
sys.path.append(os.path.abspath("./_scripts"))

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# The master toctree document.
master_doc = "index"

# Define the default role to use for links
default_role = "any"

# The set of warnings to suppress.
suppress_warnings = ["image.nonlocal_uri"]

# General information about the project.
project = "MoveIt documentation"
author = "PickNik Robotics"
copyright = "{}, {}".format(time.strftime("%Y"), author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ""
# The full version, including alpha/beta/rc tags.
release = ""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["**/_*.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.doxylink",
    "sphinx.ext.extlinks",
    "tutorialformatter",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
    "sphinx_multiversion",
    "sphinx_rtd_theme",
    "sphinx.ext.ifconfig",
    "sphinx_copybutton",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

autosectionlabel_prefix_document = True

intersphinx_mapping = {
    "ros2": ("https://docs.ros.org/en/rolling/", None),
    "catkin_pkg": ("http://docs.ros.org/en/independent/api/catkin_pkg/html", None),
    "jenkins_tools": (
        "http://docs.ros.org/en/independent/api/jenkins_tools/html",
        None,
    ),
    "rosdep": ("http://docs.ros.org/en/independent/api/rosdep/html", None),
    "rosdistro": ("http://docs.ros.org/en/independent/api/rosdistro/html", None),
    "rosinstall": ("http://docs.ros.org/en/independent/api/rosinstall/html", None),
    "rospkg": ("http://docs.ros.org/en/independent/api/rospkg/html", None),
    "vcstools": ("http://docs.ros.org/en/independent/api/vcstools/html", None),
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": -1,
    # This is the Google Analytics account used by moveit.ros.org, not picknik.ai
    "analytics_id": "UA-108532843-1",
    # Only display the logo image, do not display the project name at the top of the sidebar
    "logo_only": True,
}

html_context = {
    "display_github": True,
    "github_user": "ros-planning",
    "github_repo": "moveit2_tutorials",
    "github_version": "main/",
    "conf_py_path": "",
    "source_suffix": ".rst",
}

templates_path = [
    "_templates",
]

# smv_tag_whitelist = None

smv_branch_whitelist = r"^(main|humble)$"
smv_released_pattern = r"^refs/(heads|remotes/[^/]+)/(main|humble).*$"
smv_latest_version = "main"
smv_eol_versions = []
smv_remote_whitelist = r"^(origin|upstream)$"
smv_prefer_remote_refs = True
current_dir = os.getcwd()

distro_full_names = {
    "humble": "Humble Hawksbill",
    "rolling": "Rolling Ridley",
}

# These default values will be overridden when building multiversion
macros = {
    "DISTRO": "rolling",
    "DISTRO_TITLE": "Rolling",
    "DISTRO_TITLE_FULL": "Rolling Ridley",
    "REPOS_FILE_BRANCH": "main",
}

# Set the the browser icon
html_favicon = "_static/images/favicon.ico"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/override.css",
]

# Drop any source link suffix
html_sourcelink_suffix = ""

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "MoveItDocumentation"

html_baseurl = "https://moveit.picknik.ai/rolling/"

# Add any paths that contain custom themes here, relative to this directory.

# Links
ros_distro = "rolling"
lang = "en"
ros1_distro = "noetic"
extlinks = {
    "codedir": (
        "https://github.com/"
        + html_context["github_user"]
        + "/moveit2_tutorials/blob/"
        + html_context["github_version"]
        + "doc/%s",
        "",
    ),
    "moveit_codedir": (
        "https://github.com/"
        + html_context["github_user"]
        + "/moveit2/blob/"
        + html_context["github_version"]
        + "%s",
        "",
    ),
    "moveit_msgs_codedir": (
        "https://github.com/"
        + html_context["github_user"]
        + "/moveit_msgs/blob/ros2"
        + "/%s",
        "",
    ),
    "common_interfaces_codedir": (
        "https://github.com/ros2/common_interfaces/blob/master/%s",
        "",
    ),
    "panda_codedir": (
        "https://github.com/"
        + html_context["github_user"]
        + "/panda_moveit_config/blob/"
        + "melodic-devel"
        + "/%s",
        "",
    ),
    "moveit_resources_codedir": (
        "https://github.com/"
        + html_context["github_user"]
        + "/moveit_resources/tree/ros2"
        + "/%s",
        "",
    ),  # TODO(dlu): use ros_distro when noetic-devel branch is available
    # NEED DOCS.ROS.ORG equivalent for foxy
    "ros_documentation": (
        f"https://docs.ros.org/{lang}/{ros_distro}/%s",
        "",
    ),
    "rosdocs": ("http://docs.ros.org/" + ros1_distro + "/api/%s", ""),
    "moveit_website": ("http://moveit.ros.org/%s/", ""),
    "sensor_msgs": (
        "http://docs.ros.org/" + ros1_distro + "/api/sensor_msgs/html/msg/%s.html",
        "",
    ),
    "moveit_msgs": (
        "http://docs.ros.org/" + ros1_distro + "/api/moveit_msgs/html/msg/%s.html",
        "",
    ),
    "tf2": (
        "http://docs.ros.org/"
        + ros1_distro
        + "/api/tf2_ros/html/c++/classtf2__ros_1_1%s.html",
        "",
    ),
}
# Only used for local build, multiversion overwrites this in the smv_rewrite_configs() function
doxylink = {"cpp_api": ("build/html/api/MoveIt.tag", "api/html")}
add_function_parentheses = True


autodoc_typehints = "signature"

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "member-order": "bysource",
}

autosummary_generate = False

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False


class RedirectFrom(Directive):

    has_content = True
    template_name = "layout.html"
    redirections = {}

    @classmethod
    def register(cls, app):
        app.connect("html-collect-pages", cls.generate)
        app.add_directive("redirect-from", cls)
        return app

    @classmethod
    def generate(cls, app):
        from sphinx.builders.html import StandaloneHTMLBuilder

        if not isinstance(app.builder, StandaloneHTMLBuilder):
            return

        redirect_html_fragment = """
            <link rel="canonical" href="{base_url}/{url}" />
            <meta http-equiv="refresh" content="0; url={url}" />
            <script>
                window.location.href = '{url}';
            </script>
        """
        redirections = {
            os.path.splitext(os.path.relpath(document_path, app.srcdir))[
                0
            ]: redirect_urls
            for document_path, redirect_urls in cls.redirections.items()
        }
        redirection_conflict = next(
            (
                (canon_1, canon_2, redirs_1.intersection(redirs_2))
                for (canon_1, redirs_1), (canon_2, redirs_2) in itertools.combinations(
                    redirections.items(), 2
                )
                if redirs_1.intersection(redirs_2)
            ),
            None,
        )
        if redirection_conflict:
            canonical_url_1, canonical_url_2 = redirection_conflict[:2]
            conflicting_redirect_urls = redirection_conflict[-1]
            raise RuntimeError(
                "Documents {} and {} define conflicting redirects: {}".format(
                    canonical_url_1, canonical_url_2, conflicting_redirect_urls
                )
            )
        all_canonical_urls = set(redirections.keys())
        all_redirect_urls = {
            redirect_url
            for redirect_urls in redirections.values()
            for redirect_url in redirect_urls
        }
        conflicting_urls = all_canonical_urls.intersection(all_redirect_urls)
        if conflicting_urls:
            raise RuntimeError(
                "Some redirects conflict with existing documents: {}".format(
                    conflicting_urls
                )
            )

        for canonical_url, redirect_urls in redirections.items():
            for redirect_url in redirect_urls:
                context = {
                    "canonical_url": os.path.relpath(canonical_url, redirect_url),
                    "title": os.path.basename(redirect_url),
                    "metatags": redirect_html_fragment.format(
                        base_url=app.config.html_baseurl,
                        url=app.builder.get_relative_uri(redirect_url, canonical_url),
                    ),
                }
                yield (redirect_url, context, cls.template_name)

    def run(self):
        document_path = self.state.document.current_source
        if document_path not in RedirectFrom.redirections:
            RedirectFrom.redirections[document_path] = set()
        RedirectFrom.redirections[document_path].update(self.content)
        return []


def make_router(origin, destination):
    def _missing_reference(app, env, node, contnode):
        from docutils import nodes
        from docutils.utils import relative_path
        from sphinx.util import docname_join

        doctarget = docname_join(node["refdoc"], node["reftarget"])
        if doctarget.startswith(origin):
            routed_doctarget = doctarget.replace(origin, destination)
            if routed_doctarget in env.all_docs:
                newnode = nodes.reference("", contnode.astext(), internal=True)
                newnode["refuri"] = app.builder.get_relative_uri(
                    node["refdoc"], routed_doctarget
                )
                return newnode

    return _missing_reference


def smv_rewrite_configs(app, config):
    # When using Sphinx multiversion, there is no way at initial configuration time
    # to determine the distribution we are currently targeting (conf.py is read before
    # external defines are setup, and environment variables aren't passed through to
    # conf.py).  Instead, hook into the 'config-inited' event which is late enough
    # to rewrite the various configuration items with the current version.
    if app.config.smv_current_version != "":
        branch_distro = {
            "main": "rolling",
            "humble": "humble",
        }

        # Override default values
        branch = app.config.smv_current_version
        distro = branch_distro[branch]
        app.config.macros = {
            "DISTRO": distro,
            "DISTRO_TITLE": distro.title(),
            "DISTRO_TITLE_FULL": distro_full_names[distro],
            "REPOS_FILE_BRANCH": branch,
        }
        app.config.html_baseurl = app.config.html_baseurl + "/" + distro + "/"
        app.config.project = "MoveIt Documentation: " + distro.title()
        app.config.html_logo = "_static/images/" + distro + "-small.png"
        app.config.doxylink = {
            "cpp_api": (
                current_dir + "/build/html/" + branch + "/api/MoveIt.tag",
                "api/html",
            )
        }
    else:
        # If we are not building a multiversion build, default to the rolling logo
        app.config.html_logo = "_static/images/rolling-small.png"


def github_link_rewrite_branch(app, pagename, templatename, context, doctree):
    if app.config.smv_current_version != "":
        context["github_version"] = app.config.smv_current_version + "/"
        context["eol_versions"] = app.config.smv_eol_versions


def expand_macros(app, docname, source):
    result = source[0]
    for key, value in app.config.macros.items():
        result = result.replace(f"{{{key}}}", value)
    source[0] = result


def setup(app):
    app.connect("config-inited", smv_rewrite_configs)
    app.connect("html-page-context", github_link_rewrite_branch)
    app.connect("source-read", expand_macros)
    app.add_config_value("smv_eol_versions", [], "html")
    app.add_config_value("macros", {}, True)
    RedirectFrom.register(app)
