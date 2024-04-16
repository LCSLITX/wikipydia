import mocks
import unittest
from unittest import mock

import src.wiki_requests


class TestWikiRequests(unittest.TestCase):
    def test_get_base_url(self):
        url_en = src.wiki_requests.WikiRequests.get_base_url()
        url_pt = src.wiki_requests.WikiRequests.get_base_url('pt')
        url_it = src.wiki_requests.WikiRequests.get_base_url('it')
        self.assertEqual(url_en, "https://en.wikipedia.org/w/api.php?")
        self.assertEqual(url_pt, "https://pt.wikipedia.org/w/api.php?")
        self.assertEqual(url_it, "https://it.wikipedia.org/w/api.php?")

    @mock.patch('requests.Session.get', side_effect=mocks.mock_wiki_request_get_request)
    def test_get(self, _mock):
        url = src.wiki_requests.WikiRequests.get_base_url()
        result = src.wiki_requests.WikiRequests.get(url)
        self.assertEqual(result['mock']['pages']['123']['title'], url)

    def test_post(self):
        pass
