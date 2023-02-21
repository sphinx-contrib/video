"""Video extention to embed video in a html sphinx output."""

from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import urlparse

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

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


class video_node(nodes.General, nodes.Element):
    """Video node."""

    pass


class Video(Directive):
    """Video directive.

    Wrapper for the html <video> tag embeding all the supported options
    """

    has_content: bool = True
    required_arguments: int = 1
    optional_arguments: int = 0
    option_spec: Dict[str, Any] = {
        "alt": directives.unchanged,
        "autoplay": directives.flag,
        "controls": directives.flag,
        "height": directives.unchanged,
        "loop": directives.flag,
        "muted": directives.flag,
        "poster": directives.unchanged,
        "preload": directives.unchanged,
        "width": directives.unchanged,
    }

    def run(self) -> List[video_node]:
        """Return the video node based on the set options."""
        env = self.state.document.settings.env

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

        # add video files as images in the builder
        src = self.arguments[0]
        if not bool(urlparse(src).netloc):
            env.images.add_file("", src)

        suffix = Path(src).suffix
        if suffix not in SUPPORTED_MIME_TYPES:
            logger.warning(
                f'The provided file type ("{suffix}") is not a supported format. defaulting to ""'
            )
        type = SUPPORTED_MIME_TYPES.get(suffix, "")

        return [
            video_node(
                src=src,
                type=type,
                alt=self.options.get("alt", ""),
                autoplay="autoplay" in self.options,
                controls="controls" in self.options,
                height=height,
                loop="loop" in self.options,
                muted="muted" in self.options,
                poster=self.options.get("poster", ""),
                preload=preload,
                width=width,
            )
        ]


def visit_video_node(self, node: video_node) -> None:
    """Entry point of the video node."""
    # build the source
    html_source: str = (
        f'<source src="{node["src"]}" type="{node["type"]}">\n{node["alt"]}'
    )

    # build the video block
    attr: List[str] = [f'{k}="{node[k]}"' for k in SUPPORTED_OPTIONS if node[k]]
    html_video: str = f'<video {" ".join(attr)}>\n{html_source}\n</video>'

    self.body.append(html_video)


def depart_video_node(self, node: video_node) -> None:
    """Exit of the video node."""
    pass


def setup(app) -> None:
    """Add video node to the Sphinx builder."""
    app.add_node(video_node, html=(visit_video_node, depart_video_node))
    app.add_directive("video", Video)
