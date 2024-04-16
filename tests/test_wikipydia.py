import unittest
from unittest import mock

from tests import mock_functions
import src.wikipydia as wikipydia


class TestWikipydia(unittest.TestCase):

    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wikipydia_query_random)
    def test_query_random(self, _mock):
        result = wikipydia.Wikipydia.query_random()
        self.assertEqual(result['mock']['random'][0]['title'], '1974 in Northern Ireland')

    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wikipydia_query_search)
    def test_query_search(self, _mock):
        result = wikipydia.Wikipydia.query_search()
        self.assertEqual(result['mock']['search'][0]['title'], 'Python')
        self.assertEqual(result['mock']['search'][1]['title'], 'Python (programming language)')

    @mock.patch('requests.Session.get', side_effect=mock_functions.mock_wikipydia_query_property)
    def test_query_property(self, _mock):
        result = wikipydia.Wikipydia.query_property()
        print(result)
        self.assertEqual(result['mock']['pages']['23862']['title'], 'Python (programming language)')
        self.assertEqual(result['mock']['pages']['23862']['description'], 'General-purpose programming language')

