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

Advanced usage
--------------

the video directive supports all the optional attributes from the html tag as summurazied in the following table:

.. csv-table:: Optional Attributes
    :header: Attribute, value, Description

    ``:alt:``,``str``,Specify the text to write when the video cannot be displayed
    ``:autoplay:``,,Specifies that the video will start playing as soon as it is ready
    ``:controls:``,,Specifies that video controls should be displayed (such as a play/pause button etc).
    ``:height:``,``int``,Sets the height of the video player in pixels
    ``:loop:``,,Specifies that the video will start over again, every time it is finished
    ``:muted:``,,Specifies that the audio output of the video should be muted
    ``:poster:``,``str``, Specifies an image url to be shown while the video is downloading, or until the user hits the play button
    ``:preload:``,``str``,"Specifies if and how the author thinks the video should be loaded when the page loads. Can only be values from ``['auto', 'metadata', 'none']``"
    ``:width:``,``int``, Sets the width of the video player in pixels

They can be used as any directive option:

.. code-block:: rst

    .. video:: _static/video.mp4
        :controls:
        :loop:
        :poster: _static/image.png

.. video:: _static/video.mp4
    :controls:
    :autoplay:
    :muted:
    :loop: