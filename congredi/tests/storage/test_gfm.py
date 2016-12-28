from ...storage.gfm import resolveHtml
from ..sources import source


def test_html():
    html = resolveHtml(source)
    print(html)
