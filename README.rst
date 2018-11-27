===================
sphinxcontrib-video
===================

The video extension allows you to embed .mp4/.webm/etc videos as defined by the
HTML5 standard. It's just a wrapper around:

::

  <video width="320" height="240" controls>
    <source src="movie.mp4" type="video/mp4">
  Your browser does not support the video tag.
  </video>



Parameters
===============

The extension should expose pretty much all parameters from the HTML5 <video/> 
tag.

Example::

    .. video:: path/to/video.mp4
       :width: 500
       :height: 300
       :autoplay:
       :nocontrols:

Please note that the width, height, autoplay and nocontrols parameters are all 
optional.

Installing
==========

As usual with sphinx extensions, remember to add them to your config:

::

  extensions = [
      'sphinxcontrib.video'
  ]


Links
-----

- Source: https://github.com/sphinx-contrib/sphinxcontrib-video
- Bugs: https://github.com/sphinx-contrib/sphinxcontrib-video/issues
