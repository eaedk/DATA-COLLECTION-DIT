# Rest API
# Generating Get URLs
import json

import requests

URL1 = "https://api.datamuse.com/words"
URL2 = "https://www.google.com/search"


def divider(n=20):
    return '-' * n


if __name__ == '__main__':
    # Generating URLs with pass params key (1)
    # Use Dict data structure to construct a params
    key_pairs = {'rel_rhy': 'funny'}
    page = requests.get(URL1, params=key_pairs)
    print(divider())
    print(page.text[:150])
    print(divider())
    print(page.url)
    print(divider())
    print('\n')

    # Generating URLs with pass params key (2)
    # Use Dict data structure to construct a params
    params = {'q': 'violins and guitars', 'tbm': 'isch'}
    result = requests.get(URL2, params=params)
    print(divider())
    print(result.url)
    print(divider())
    print(result.text)
