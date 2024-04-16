"""This module provides unit tests for the wikipydia module."""
import unittest
from unittest import mock

from tests import mock_functions
from src import wikipydia


class TestWikipydia(unittest.TestCase):
    """This class provides unittests for the wikipydia class."""
    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wikipydia_query_random)
    def test_query_random(self, _mock):
        """This function tests query_random method of Wikipydia class."""
        result = wikipydia.Wikipydia.query_random()
        self.assertEqual(result['mock']['random'][0]['title'], '1974 in Northern Ireland')

    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wikipydia_query_search)
    def test_query_search(self, _mock):
        """This function tests query_search method of Wikipydia class."""
        result = wikipydia.Wikipydia.query_search()
        self.assertEqual(result['mock']['search'][0]['title'], 'Python')
        self.assertEqual(result['mock']['search'][1]['title'], 'Python (programming language)')

    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wikipydia_query_property)
    def test_query_property(self, _mock):
        """This function tests query_property method of Wikipydia class."""
        result = wikipydia.Wikipydia.query_property()
        self.assertEqual(result['mock']['pages']['23862']['title'], 'Python (programming language)')
        self.assertEqual(result['mock']['pages']['23862']['description'], 'General-purpose programming language')
