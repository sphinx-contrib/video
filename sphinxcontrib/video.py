#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from docutils import nodes
from docutils.parsers.rst import directives, Directive

def get_option(options, key, default):
    if key not in options.keys():
        return default

    if type(default) == type(True):
        return True
    else:   
        return options[key]

class video(nodes.General, nodes.Element): pass

class Video(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 5
    final_argument_whitespace = False
    option_spec = {
        "alt": directives.unchanged,
        "width": directives.unchanged,
        "height": directives.unchanged,
        "autoplay": directives.flag,
        "nocontrols": directives.flag,
        "loop": directives.flag,
        "muted": directives.flag,
        "additionalsource": directives.unchanged
    }

    def run(self):
        alt = get_option(self.options, "alt", "Video")
        width = get_option(self.options, "width", "")
        height = get_option(self.options, "height", "")
        autoplay = get_option(self.options, "autoplay", False)
        nocontrols = get_option(self.options, "nocontrols", False)
        loop = get_option(self.options, "loop", False)
        muted = get_option(self.options, "muted", False)
        additionalsource = get_option(self.options, "additionalsource", "")
        
        return [video(
            path=self.arguments[0],
            alt=alt, 
            width=width,
            height=height, 
            autoplay=autoplay, 
            nocontrols=nocontrols, 
            loop=loop, 
            muted=muted, 
            additionalsource=additionalsource
            )]

def visit_video_node(self, node):
    extension = os.path.splitext(node["path"])[1][1:]

    logger = logging.getLogger(__name__)
    if node["additionalsource"] == "": 
        logger = logging.getLogger(__name__)
        logger.warning('Video tag is missing additional source. This could break compatibility with some browsers.', location=node)

    html_block = '''
    <video {width} {height} {nocontrols} {autoplay} {muted} {loop}>
    <source src="{path}" type="video/{filetype}">
    {additionalsource}
    {alt}
    </video>
    '''.format(
        width="width=\"" + node["width"] + "\"" if node["width"] else "", 
        height="height=\"" + node["height"] + "\"" if node["height"] else "",
        path=node["path"], 
        filetype=extension,
        alt=node["alt"],
        autoplay="autoplay" if node["autoplay"] else "",
        nocontrols="" if node["nocontrols"] else "controls",
        muted="muted" if node["muted"] else "",
        loop="loop" if node["loop"] else "", 
        additionalsource="<source src=\"" + node["additionalsource"] + "\" type=\"video/" + os.path.splitext(node["additionalsource"])[1][1:] + "\">" if node["additionalsource"] else ""
        )
    self.body.append(html_block)

def depart_video_node(self, node):
    pass

def setup(app):
    app.add_node(video, html=(visit_video_node, depart_video_node))
    app.add_directive("video", Video)
