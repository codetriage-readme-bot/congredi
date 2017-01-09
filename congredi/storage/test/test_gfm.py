import unittest
from ...storage.gfm import resolveHtml
from ...tests.sources import source

# pylint: disable=no-self-use


class test_html(unittest.TestCase):

    def test_html(self):
        html = resolveHtml(source)
        print(html)
