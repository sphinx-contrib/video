sphinxcontrib-video
===================

.. image:: https://img.shields.io/badge/License-Apache%202.0-yellow.svg
    :target: https://github.com/sphinx-contrib/video/blob/master/LICENSE
    :alt: License: MIT

.. image:: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg
   :target: https://conventionalcommits.org
   :alt: conventional commit

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black badge

.. image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg
   :target: https://github.com/prettier/prettier
   :alt: prettier badge

.. image:: https://img.shields.io/pypi/v/sphinxcontrib-video?color=blue&logo=python&logoColor=white
   :alt: PyPI
   :target: https://pypi.org/project/sphinxcontrib-video/

.. image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-video?logo=python&logoColor=white
   :alt: PyPI - Python Version
   :target: https://pypi.org/project/sphinxcontrib-video/

.. image:: https://img.shields.io/readthedocs/sphinxcontrib-video?logo=readthedocs&logoColor=white
   :alt: Read the Docs
   :target: https://readthedocs.org/projects/sphinxcontrib-video/

.. image:: https://img.shields.io/codecov/c/github/sphinx-contrib/video?logo=codecov&logoColor=white
   :alt: Codecov
   :target: https://app.codecov.io/gh/sphinx-contrib/video

.. image:: https://img.shields.io/github/actions/workflow/status/sphinx-contrib/video/unit.yaml?logo=github&logoColor=white
   :alt: GitHub Workflow Status
   :target: https://github.com/sphinx-contrib/video/actions/workflows/unit.yaml

The video extension allows you to embed ``.mp4``/``.webm``/``.ogg`` videos as defined by the HTML5 standard. It's a wrapper around the ``<video>`` tag. using a simple directive as:

.. code-block:: rst

  .. video:: movie.mp4

will be rendered as:

.. code-block:: html

   <video>
      <source src="movie.mp4" type="video/mp4">
   </video>

The extension exposes pretty much all parameters from the HTML5 ``<video/>`` tag.

More information about installation and usage in our `documentation quickstart <https://sphinxcontrib-video.readthedocs.io/en/latest/quickstart.html>`__.
