"""Test sphinxcontrib.video extension"""

import pytest
from bs4 import BeautifulSoup

@pytest.mark.sphinx(testroot='video')
def test_video(app, status, warning, file_regression):

    app.builder.build_all()

    html = (app.outdir / 'mp4.html').read_text(encoding='utf8')
    html = BeautifulSoup(html, "html.parser")
    video = html.select("video")[0].prettify()
    file_regression.check(video, basename="video_no_options", extension=".html")

@pytest.mark.sphinx(testroot='video')
def test_video_options(app, status, warning, file_regression):

    app.builder.build_all()

    html = (app.outdir / 'mp4_options.html').read_text(encoding='utf8')
    html = BeautifulSoup(html, "html.parser")
    video = html.select("video")[0].prettify()
    file_regression.check(video, basename="video_options", extension=".html")

@pytest.mark.sphinx(testroot='video-warnings')
def test_wrong_format(app, status, warning, file_regression):

    app.builder.build_all()

    assert "The provided file type (.mkv) is not a supported format. defaulting to ''" in warning.getvalue()

    # test the video is still existing
    html = (app.outdir / 'wrong_format.html').read_text(encoding='utf8')
    html = BeautifulSoup(html, "html.parser")
    video = html.select("video")[0].prettify()
    file_regression.check(video, basename="video_wrong_format", extension=".html")

@pytest.mark.sphinx(testroot='video-warnings')
def test_wrong_height(app, status, warning, file_regression):

    app.builder.build_all()

    # test the video is still existing
    html = (app.outdir / 'wrong_height.html').read_text(encoding='utf8')
    html = BeautifulSoup(html, "html.parser")
    video = html.select("video")[0].prettify()
    file_regression.check(video, basename="video_no_options", extension=".html")

@pytest.mark.sphinx(testroot='video-warnings')
def test_wrong_width(app, status, warning, file_regression):

    app.builder.build_all()

    # test the video is still existing
    html = (app.outdir / 'wrong_width.html').read_text(encoding='utf8')
    html = BeautifulSoup(html, "html.parser")
    video = html.select("video")[0].prettify()
    file_regression.check(video, basename="video_no_options", extension=".html")

@pytest.mark.sphinx(testroot='video-warnings')
def test_wrong_preload(app, status, warning, file_regression):

    app.builder.build_all()

    # test the video is still existing
    html = (app.outdir / 'wrong_preload.html').read_text(encoding='utf8')
    html = BeautifulSoup(html, "html.parser")
    video = html.select("video")[0].prettify()
    file_regression.check(video, basename="video_no_options", extension=".html")