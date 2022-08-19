import json
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.youtube.com/results'


class DataSouper(object):
    @classmethod
    def httpFetcher(cls,
                    URL,
                    params=None,
                    headers=None):
        with requests.Session() as session:
            result = session.get(URL,
                                 params=params,
                                 headers=headers)
            result = result.text
            return result


if __name__ == '__main__':
    result = DataSouper.httpFetcher(
        BASE_URL,
        params={'search_query': 'film+complet+en+français'},
        headers={})
    print(result)
