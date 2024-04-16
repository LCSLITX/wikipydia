"""This module provides unit tests for the wiki_requests module."""
import unittest
from unittest import mock


from tests import mock_functions
from src import wiki_requests


class TestWikiRequests(unittest.TestCase):
    """This class provides unittests for the wiki_requests class."""

    def test_get_base_url(self):
        """This function tests if the get_base_url static method of wiki_requests class is working properly."""
        url_en = wiki_requests.WikiRequests.get_base_url()
        url_pt = wiki_requests.WikiRequests.get_base_url('pt')
        url_it = wiki_requests.WikiRequests.get_base_url('it')
        self.assertEqual(url_en, "https://en.wikipedia.org/w/api.php?")
        self.assertEqual(url_pt, "https://pt.wikipedia.org/w/api.php?")
        self.assertEqual(url_it, "https://it.wikipedia.org/w/api.php?")

    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wiki_request_get_request)
    def test_get(self, _mock):
        """This function tests if the get static method of wiki_requests class is working properly."""
        url = wiki_requests.WikiRequests.get_base_url()
        result = wiki_requests.WikiRequests.get(url)
        self.assertEqual(result['mock']['pages']['123']['title'], url)
