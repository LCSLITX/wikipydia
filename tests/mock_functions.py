"""This module provide mock functions to tests."""
from requests.models import Response


def mock_wiki_request_get_request(url, params: str = None, headers: str = None):
    """Mock for requests.Session.get"""
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    content = f'{{"mock": {{"pages": {{"123": {{"title": "{url}" }} }} }} }}'
    resp._content = bytes(content, 'utf-8')
    return resp


def mock_wikipydia_query_random(url, params: str = None, headers: str = None):
    """Mock for requests.Session.get"""
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    content = (f'{{"batchcomplete": "",'
               f'"continue": {{"rncontinue": "0.001968939888|0.001969201132|58438612|0", "continue": "-||"}},'
               f'"mock": {{"random": [{{"id": 9652336, "ns": 0, "title": "1974 in Northern Ireland",'
               f'"url": "{url}" }}] }} }}'
               )
    resp._content = bytes(content, 'utf-8')
    return resp


def mock_wikipydia_query_search(url, params: str = None, headers: str = None):
    """Mock for requests.Session.get"""
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    content = (f'{{"batchcomplete": "",'
               f'"continue": {{"sroffset": 10, "continue": "-||"}},'
               f'"mock": {{"searchinfo": {{"totalhits": 12549}},'
               f'"search": ['
               f'{{"ns": 0, "title": "Python", "pageid": 46332325, "size": 1968, "wordcount": 271,'
               f'"snippet": "{url}", "timestamp": "2024-03-14T04:50:24Z"}},'
               f'{{"ns": 0, "title": "Python (programming language)", "pageid": 23862, "size": 163077,'
               f'"wordcount": 13251, "snippet": "Python is a high-level, general-purpose programming language.",'
               f'"timestamp": "2024-04-12T20:38:35Z"}}]}}}}'
               )
    resp._content = bytes(content, 'utf-8')
    return resp


def mock_wikipydia_query_property(url, params: str = None, headers: str = None):
    """Mock for requests.Session.get"""
    resp = Response()
    resp.url = url
    resp.code = 'success'
    resp.status_code = 200
    resp.headers = {'content-type': 'application/json'}
    content = (f'{{"batchcomplete": "",'
               f'"mock": {{"pages": {{"23862": {{"pageid": 23862, "ns": 0, "title": "Python (programming language)",'
               f'"description": "General-purpose programming language", "url": "{url}" }} }} }} }}')
    resp._content = bytes(content, 'utf-8')
    return resp
