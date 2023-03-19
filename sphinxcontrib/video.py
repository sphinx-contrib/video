"""Video extention to embed video in a html sphinx output."""

from pathlib import Path
from typing import Any, Dict, List, Tuple
from urllib.parse import urlparse

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, SphinxTranslator

__author__ = "Raphael Massabot"
__version__ = "0.0.0"

logger = logging.getLogger(__name__)

SUPPORTED_MIME_TYPES: Dict[str, str] = {
    ".mp4": "video/mp4",
    ".ogm": "video/ogg",
    ".ogv": "video/ogg",
    ".ogg": "video/ogg",
    ".webm": "video/webm",
}
"Supported mime types of the link tag"

SUPPORTED_OPTIONS: List[str] = [
    "autoplay",
    "controls",
    "height",
    "loop",
    "muted",
    "poster",
    "preload",
    "width",
]
"List of the supported options attributes"


def get_video(src: str, env: BuildEnvironment) -> Tuple[str, str]:
    """Return video and suffix.

    Load the video to the static directory if necessary and process the suffix. Raise a warning if not supported but do not stop the computation.

    Args:
        src: The source of the video file (can be local or url)
        env: the build environment

    Returns:
        the src file, the extention suffix
    """
    if not bool(urlparse(src).netloc):
        env.images.add_file("", src)

    suffix = Path(src).suffix
    if suffix not in SUPPORTED_MIME_TYPES:
        logger.warning(
            f'The provided file type ("{suffix}") is not a supported format. defaulting to ""'
        )
    type = SUPPORTED_MIME_TYPES.get(suffix, "")

    return (src, type)


class video_node(nodes.General, nodes.Element):
    """Video node."""

    pass


class Video(SphinxDirective):
    """Video directive.

    Wrapper for the html <video> tag embeding all the supported options
    """

    has_content: bool = True
    required_arguments: int = 1
    optional_arguments: int = 1
    option_spec: Dict[str, Any] = {
        "alt": directives.unchanged,
        "autoplay": directives.flag,
        "nocontrols": directives.flag,
        "height": directives.unchanged,
        "loop": directives.flag,
        "muted": directives.flag,
        "poster": directives.unchanged,
        "preload": directives.unchanged,
        "width": directives.unchanged,
    }

    def run(self) -> List[video_node]:
        """Return the video node based on the set options."""
        env: BuildEnvironment = self.env

        # check options that need to be specific values
        height: str = self.options.get("height", "")
        if height and not height.isdigit():
            logger.warning(
                f'The provided height ("{height}") is ignored as it\'s not an integer'
            )
            height = ""

        width: str = self.options.get("width", "")
        if width and not width.isdigit():
            logger.warning(
                f'The provided width ("{width}") is ignored as it\'s not an integer'
            )
            width = ""

        preload: str = self.options.get("preload", "auto")
        valid_preload = ["auto", "metadata", "none"]
        if preload not in valid_preload:
            logger.warning(
                f'The provided preload ("{preload}") is not an accepted value. defaulting to "auto"'
            )
            preload = "auto"

        # add the primary video files as images in the builder
        primary_src = get_video(self.arguments[0], env)

        # add the secondary video files as images in the builder if necessary
        secondary_src = None
        if len(self.arguments) == 2:
            secondary_src = get_video(self.arguments[1], env)
        elif env.config.video_enforce_extra_source is True:
            logger.warning(
                f'A secondary source should be provided for "{self.arguments[0]}"'
            )

        return [
            video_node(
                primary_src=primary_src,
                secondary_src=secondary_src,
                alt=self.options.get("alt", ""),
                autoplay="autoplay" in self.options,
                controls="nocontrols" not in self.options,
                height=height,
                loop="loop" in self.options,
                muted="muted" in self.options,
                poster=self.options.get("poster", ""),
                preload=preload,
                width=width,
            )
        ]


def visit_video_node_html(translator: SphinxTranslator, node: video_node) -> None:
    """Entry point of the html video node."""
    # start the video block
    attr: List[str] = [f'{k}="{node[k]}"' for k in SUPPORTED_OPTIONS if node[k]]
    html: str = f"<video {' '.join(attr)}>"

    # build the sources
    html_source = '<source src="{}" type="{}">'
    html += html_source.format(*node["primary_src"])
    if node["secondary_src"] is not None:
        html += html_source.format(*node["secondary_src"])

    # add the alternative message
    html += node["alt"]

    translator.body.append(html)


def depart_video_node_html(translator: SphinxTranslator, node: video_node) -> None:
    """Exit of the html video node."""
    translator.body.append("</video>")


def visit_video_node_unsuported(translator: SphinxTranslator, node: video_node) -> None:
    """Entry point of the ignored video node."""
    logger.warning(
        f"video {node['primary_src']}: unsupported output format (node skipped)"
    )
    raise nodes.SkipNode


def setup(app: Sphinx) -> Dict[str, bool]:
    """Add video node and parameters to the Sphinx builder."""
    app.add_config_value("video_enforce_extra_source", False, "html")
    app.add_node(
        video_node,
        html=(visit_video_node_html, depart_video_node_html),
        epub=(visit_video_node_unsuported, None),
        latex=(visit_video_node_unsuported, None),
        man=(visit_video_node_unsuported, None),
        texinfo=(visit_video_node_unsuported, None),
        text=(visit_video_node_unsuported, None),
    )
    app.add_directive("video", Video)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
