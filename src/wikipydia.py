"""This module is a wrapper for Wikipedia API."""
import wiki_requests


class Wikipydia:
    """
    Wikipydia class is a wrapper for consuming the Wikipedia API.
    """

    @staticmethod
    def query_property(prop: str = 'info', titles: str = 'Main Page', lang: str = 'en', rformat: str = 'json') -> str:
        """
        Make a Property query request to Wikipedia. Used to retrieve specific property(ies) of an article.

        Check out these urls for more information:

        - https://en.wikipedia.org/w/api.php?action=help&modules=query;
        - https://www.mediawiki.org/wiki/API:Query.

        :param prop: Wikipedia property(ies) (default: 'description'). It may receive more than one property and all
         of them should be separated by a pipe sign '|'. E.g. 'info|description'.
        :type prop: str
        :param titles: Wikipedia title(s) of an article (default: 'Main Page'). It may receive more than one title
         and all of them should be separated by a pipe sign '|'. E.g. 'James Bond|Mount Everest'.
        :type titles: str
        :param lang: Wikipedia language (default: 'en').
        :type lang: str
        :param rformat: Wikipedia request format (default: 'json').
        :type rformat: str
        :return: Response: A JSON containing Wikipedia API results.
        """
        url = wiki_requests.WikiRequests.get_base_url(lang)

        params = {
            'action': 'query',
            'format': rformat,
            'prop': prop,
            'titles': titles,
        }

        resp = wiki_requests.WikiRequests.get(url, params)
        return resp

    @staticmethod
    def query_search(
            srsearch: str = 'Python',
            srwhat: str = 'text',
            sroffset: int = 0,
            lang: str = 'en',
            rformat: str = 'json'
    ) -> str:
        """
        Make a List query request to Wikipedia. Used to retrieve search results for a specific term.
        Check out this url for more information: https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bsearch.
        :param srsearch: Wikipedia page title or content to search for (default: 'Python').
        :type srsearch: str
        :param srwhat: Wikipedia page title (default: 'text'). It may receive one of the following
            values: nearmatch, text, title.
        :type srwhat: str
        :param sroffset: Wikipedia search offset (default: 0).
        :type sroffset: int
        :param lang: Wikipedia language (default: 'en')
        :type lang: str
        :param rformat: Wikipedia request format (default: 'json')
        :type rformat: str
        :return: Response: A JSON containing Wikipedia API results.
        """
        url = wiki_requests.WikiRequests.get_base_url(lang)

        params = {
            'action': 'query',
            'list': 'search',
            'format': rformat,
            'srsearch': srsearch,
            'sroffset': sroffset,
            'srwhat': srwhat,
        }

        resp = wiki_requests.WikiRequests.get(url=url, params=params)
        return resp

    @staticmethod
    def query_random(from_namespace: int = 0, random_limit: int = 1, lang: str = 'en', rformat: str = 'json') -> str:
        """
        Make a List query request to Wikipedia. Used to retrieve random results from a specific namespace.

        Check out this url for more information:

        - https://www.mediawiki.org/wiki/Manual:Namespace;
        - https://en.wikipedia.org/w/api.php?action=help&modules=query%2Brandom.

        :param from_namespace: Wikipedia namespace (default: 0). Namespaces goes from -2 to 15. 0 is the main namespace,
        for real content articles.
        :type from_namespace: int
        :param random_limit: Wikipedia limit (default: 1). In case of numbers bigger than one, only the first result
        will be random.
        :type random_limit: int
        :param lang: Wikipedia language (default: 'en')
        :type lang: str
        :param rformat: Wikipedia request format (default: 'json')
        :type rformat: str
        :return: Response: A JSON containing Wikipedia API results.
        """
        url = wiki_requests.WikiRequests.get_base_url(lang)

        params = {
            'action': 'query',
            'list': 'random',
            'format': rformat,
            'rnnamespace': from_namespace,
            'rnlimit': random_limit,
        }

        resp = wiki_requests.WikiRequests.get(url=url, params=params)
        return resp
