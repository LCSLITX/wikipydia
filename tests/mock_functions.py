from requests.models import Response


def mock_wiki_request_get_request(url, params: str = None, headers: str = None):
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    s = f'{{"mock": {{"pages": {{"123": {{"title": "{url}" }} }} }} }}'
    resp._content = bytes(s, 'utf-8')
    return resp


def mock_wikipydia_query_random(url, params: str = None, headers: str = None):
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    s = f'{{"batchcomplete": "", "continue": {{"rncontinue": "0.001968939888|0.001969201132|58438612|0", "continue": "-||"}}, "mock": {{"random": [{{"id": 9652336, "ns": 0, "title": "1974 in Northern Ireland"}}] }} }}'
    resp._content = bytes(s, 'utf-8')
    return resp


def mock_wikipydia_query_search(url, params: str = None, headers: str = None):
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    s = f'{{"batchcomplete": "", "continue": {{"sroffset": 10, "continue": "-||"}}, "mock": {{"searchinfo": {{"totalhits": 12549}}, "search": [{{"ns": 0, "title": "Python", "pageid": 46332325, "size": 1968, "wordcount": 271, "snippet": "Look up Python or python in Wiktionary, the free dictionary. Python may refer to: Pythonidae, a family of nonvenomous snakes found in Africa, Asia, and", "timestamp": "2024-03-14T04:50:24Z"}}, {{"ns": 0, "title": "Python (programming language)", "pageid": 23862, "size": 163077, "wordcount": 13251, "snippet": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation", "timestamp": "2024-04-12T20:38:35Z"}}]}}}}'
    resp._content = bytes(s, 'utf-8')
    return resp


def mock_wikipydia_query_property(url, params: str = None, headers: str = None):
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    s = f'{{"batchcomplete": "", "mock": {{"pages": {{"23862": {{"pageid": 23862, "ns": 0, "title": "Python (programming language)", "description": "General-purpose programming language", "descriptionsource": "local"}} }} }} }}'
    resp._content = bytes(s, 'utf-8')
    return resp
