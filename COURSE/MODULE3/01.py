# Rest API
# Fetching Data with requests modules
import json

import requests


def divider(n=20):
    return '-' * n


if __name__ == '__main__':
    # Execute Request with requests Module
    page = requests.get('https://api.datamuse.com/words?rel_rhy=funny')
    print(divider())
    print(type(page))
    print(divider())
    print('\n')

    # Print the first 150 Characters
    print(page.text[:150])
    print(divider())
    print('\n')

    # Print the page variable URL
    print(page.url)
    print(divider())
    print('\n')

    # Print the response in JSON format
    JSON_RES = page.json()
    print(JSON_RES)
    print(divider())
    print('\n')

    # Print format response
    result = json.dumps(JSON_RES, indent=4)
    print(result)
    print(divider())
