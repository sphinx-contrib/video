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
    ``:controlslist:``,``str``, "Specifies the controls to show on the media element. Can only be one or more of values from ``['nodownload', 'nofullscreen', 'noremoteplayback']``"
    ``:height:``,``int``,Sets the height of the video player in pixels (ignored if relative width is used)
    ``:loop:``,,"Specifies that the video will start over again, every time it is finished"
    ``:muted:``,,Specifies that the audio output of the video should be muted
    ``:poster:``,``str``, "Specifies an image url to be shown while the video is downloading, or until the user hits the play button"
    ``:preload:``,``str``,"Specifies if and how the author thinks the video should be loaded when the page loads. Can only be values from ``['auto', 'metadata', 'none']``"
    ``:width:``,``int``\ [``%``\ ], Sets the width of the video player in pixels or relative to the page's width if a percentage
    ``:playsinline:``,,Specifies that the video will play in-line (instead of full-screen) on small devices.
    ``:class:``,``str``, Set extra class to the video html tag
    ``:align:``,``str``, "Sets the horizontal alignment. Can only be values from ``['default', 'left', 'center', 'right']``"
    ``:caption:``,``str``, Set the caption text under video
    ``:figwidth:``,``str``, Set the maximum width of caption text. It is defined as the same of 'figwidth' `in figure <https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure>`_. It will be disabled when 'caption' is not set.

They can be used as any directive option:

.. code-block:: rst

    .. video:: _static/video.mp4
        :nocontrols:
        :autoplay:
        :playsinline:
        :muted:
        :loop:
        :poster: _static/image.png
        :width: 100%

.. video:: _static/video.mp4
    :nocontrols:
    :autoplay:
    :playsinline:
    :muted:
    :loop:
    :width: 100%
    :poster: _static/image.png

And using the ``:class:`` parameter in combination with custom css, you can change the display of the html ``<video>`` tag:

.. code-block:: rst

    .. video:: _static/video.mp4
        :class: video-bordered

.. video:: _static/video.mp4
    :class: video-bordered

Alignment:

.. code-block:: rst

    .. video:: _static/video.mp4
        :align: left

.. video:: _static/video.mp4
    :align: left

.. code-block:: rst

    .. video:: _static/video.mp4
        :align: center

.. video:: _static/video.mp4
    :align: center

.. code-block:: rst

    .. video:: _static/video.mp4
        :align: right

.. video:: _static/video.mp4
    :align: right

For consistency with previous versions, which not support align, the default value of align is set to `left` when nothing is set.
If you want to use the alignment defined by your theme, you need to, manually, set it to `default`:

.. code-block:: rst

    .. video:: _static/video.mp4
        :align: default

.. video:: _static/video.mp4
    :align: default

Caption:

.. code-block:: rst

    .. video:: _static/video.mp4
        :align: center
        :caption: The caption text

.. video:: _static/video.mp4
    :align: center
    :caption: The caption text

Use figwidth to set the maximum width of the caption text if the video is narrow:

.. code-block:: rst

    .. video:: _static/video.mp4
        :width: 300
        :figwidth: 60%
        :align: center
        :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

.. video:: _static/video.mp4
    :width: 300
    :figwidth: 60%
    :align: center
    :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

The width of video is not controlled by 'figwidth', you need to use 'width' to control it. For example, if you don't set the 'width', the following problems may occur: The video with is greater than 'figwith', resulting in results that are not aligned as expected.

.. code-block:: rst

    .. video:: _static/video.mp4
        :figwidth: 60%
        :align: center
        :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

.. video:: _static/video.mp4
    :figwidth: 60%
    :align: center
    :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

When the 'width' is set to a percentage, the percent number indicates the relative to 'figwidth':

.. code-block:: rst

    .. video:: _static/video.mp4
        :width: 100%
        :figwidth: 60%
        :align: center
        :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

.. video:: _static/video.mp4
    :width: 100%
    :figwidth: 60%
    :align: center
    :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

When 'caption' is set, and 'align' is 'left' or 'right', the video will be float to text in some themes.

.. code-block:: rst

    .. video:: _static/video.mp4
        :width: 95%
        :figwidth: 65%
        :align: left
        :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

    long long text...

.. video:: _static/video.mp4
    :width: 95%
    :figwidth: 65%
    :align: left
    :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text

.. code-block:: rst

    .. video:: _static/video.mp4
        :width: 95%
        :figwidth: 65%
        :align: right
        :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

    long long text...

.. video:: _static/video.mp4
    :width: 95%
    :figwidth: 65%
    :align: right
    :caption: The caption text text xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx

long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text
long long text long long text long long text long long text long long text long long text long long text


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
