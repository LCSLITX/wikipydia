"""This module handle requests to Wikipedia API."""
import requests


class WikiRequests:
    """
    WikiRequest class is responsible for making requests to the Wikipedia API.

    Useful Links:

    - Tutorial: https://www.mediawiki.org/wiki/API:Tutorial.
    - Etiquette: https://www.mediawiki.org/wiki/API:Etiquette.
    - Help: https://en.wikipedia.org/w/api.php?action=help
    """
    base_url: str = 'https://{0}.wikipedia.org/w/api.php?'
    headers: dict = {'User-Agent': 'src/0.0 (https://github.com/LCSLITX/wikipydia)'}

    @staticmethod
    def get_base_url(language: str = 'en') -> str:
        """
        Returns the Wikipedia API base URL.
        :param language: Wikipedia language.
        :type language: str
        :return: Wikipedia API base URL.
        """
        return str.format(WikiRequests.base_url, language)

    @staticmethod
    def get(url: str, params: dict = None, headers: dict = None):
        """
        Sends a GET request to Wikipedia.
        :param url:
        :param params:
        :param headers:
        :return: JSON response.
        """
        if headers is None:
            headers = WikiRequests.headers

        req_session = requests.session()
        resp = req_session.get(url=url, params=params, headers=headers)
        return resp.json()
