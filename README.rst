sphinxcontrib-video
===================

.. image:: https://img.shields.io/badge/License-Apache%202.0-yellow.svg
    :target: https://github.com/sphinx-contrib/video/blob/master/LICENSE
    :alt: License: MIT

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black badge

.. image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg
   :target: https://github.com/prettier/prettier
   :alt: prettier badge

The video extension allows you to embed ``.mp4``/``.webm``/``.ogg`` videos as defined by the HTML5 standard. It's a wrapper around the ``<video>`` tag. using a simple directive as:

.. code-block:: rst

  .. video:: movie.mp4

will be rendered as:

.. code-block:: html

   <video>
      <source src="movie.mp4" type="video/mp4">
   </video>

The extension exposes pretty much all parameters from the HTML5 ``<video/>`` tag.

More information about installation and usage in our `documentation <#>`__.
