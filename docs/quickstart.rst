Quickstart
==========

This section contains basic information about **sphinxcontrib.video** to get you started.

Installation
------------

Use ``pip`` to install **sphinxcontrib-video** in your environment:

.. code-block:: console

    pip install sphinxcontrib-video

Extension setup
---------------

Enable the extension
^^^^^^^^^^^^^^^^^^^^

After installing **sphinxcontrib-video**, add ``sphinxcontrib.video`` to the list of extensions
in your ``conf.py`` file:

.. code-block:: python

    extensions = [
        #[...]
        "sphinxcontrib.video",
    ]

video directive
---------------

You can now add video directly in your documentation:

.. code-block:: rst

    .. video:: _static/video.mp4

.. video:: _static/video.mp4

Options
-------

the video directive supports all the optional attributes from the html tag as summurazied in the following table:

.. csv-table:: Optional Attributes
    :header: Attribute, value, Description

    ``:alt:``,``str``,Specify the text to write when the video cannot be displayed
    ``:autoplay:``,,Specifies that the video will start playing as soon as it is ready
    ``:nocontrols:``,,Specifies that video controls should not be displayed (such as a play/pause button etc).
    ``:height:``,``int``,Sets the height of the video player in pixels
    ``:loop:``,,Specifies that the video will start over again, every time it is finished
    ``:muted:``,,Specifies that the audio output of the video should be muted
    ``:poster:``,``str``, Specifies an image url to be shown while the video is downloading, or until the user hits the play button
    ``:preload:``,``str``,"Specifies if and how the author thinks the video should be loaded when the page loads. Can only be values from ``['auto', 'metadata', 'none']``"
    ``:width:``,``int``, Sets the width of the video player in pixels
    ``:class:``,``str``, Set extra class to the video html tag

They can be used as any directive option:

.. code-block:: rst

    .. video:: _static/video.mp4
        :nocontrols:
        :loop:
        :poster: _static/image.png

.. video:: _static/video.mp4
    :nocontrols:
    :autoplay:
    :muted:
    :loop:

And using the ``:class:`` parameter in combination with custom css, you can change the display of the html ``<video>`` tag:

.. code-block:: rst

    .. video:: _static/video.mp4
        :class: video-bordered

.. video:: _static/video.mp4
    :class: video-bordered

Advanced Usage
--------------

The browser used by the user may not support the codec of the primary source set in the directive. The ``<video>`` tag offers the possibility to add multiple sources, the first one compatible being the one displayed on screen. To use this options simply add the alternative source as a second argument to your video:

.. code-block:: rst

    .. video:: _static/video.webm _static/video.mp4

.. video:: _static/video.webm _static/video.mp4

.. note::

    to enforce this behavior set the sphinx parameter ``video_enforce_extra_source`` to ``True`` in your conf.py, it will then raise a warning when a secondary source is missing.

    .. code-block:: python

        # conf.py

        video_enforce_extra_source = True