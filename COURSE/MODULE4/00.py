from typing import List, Union

import bs4
import requests
from bs4 import BeautifulSoup


def divider(n=25):
    return '-' * n


class DataSouper(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result

    @classmethod
    def soupData(cls, result):
        return BeautifulSoup(
            result,
            'html.parser')


if __name__ == '__main__':
    URL = 'https://dit.sn/'
    result = DataSouper.httpFetcher(URL)
    souper = DataSouper.soupData(result)
    print(divider(35))

    # Get all H2
    # Use .find_all()/.find()
    # Use the Tag to get all data
    print(divider(35))
    print(souper.find_all('h1'))
    print(divider(35))
    print(souper.find_all('h2'))
    print(divider(35))
    print(souper.find_all('h3'))
    print(divider(35))
    print('\n')

    # Get all Links with ID
    # Use .find_all()/.find()
    # Use the ID attribute to get data
    print(divider(35))
    print(souper.find_all(id='menu-item-31890'))
    print(divider(35))
    print(souper.find_all(id='menu-item-28943'))
    print(divider(35))
    print(souper.find_all(id='menu-item-30993'))
    print(divider(35))
    print('\n')

    # Get all Links with ID
    # Use .find_all()/.find()
    # Use the ID attribute to get data
    print(divider(35))
    print(souper.find_all(attrs={'id': 'menu-item-31890'}))
    print(divider(35))
    print(souper.find_all(attrs={'id': 'menu-item-28943'}))
    print(divider(35))
    print(souper.find_all(attrs={'id': 'menu-item-30993'}))
    print(divider(35))
    print('\n')

    # Get all soup contents
    # Use .find_all()/.find()
    # Use the ID attribute to get data
    print(divider(35))
    var = souper.find(attrs={'id': 'menu-item-31890'})
    print(var)
    print(type(var))
    print(var.contents)
    print(divider(35))
    print('\n')

    # Get all soup parent
    # Use .find_all()/.find()
    # Use .parent
    # Use the ID attribute to get data
    print(divider(35))
    var = souper.find(attrs={'id': 'menu-item-31890'})
    print(var.parent)
    print(divider(35))
    print('\n')

    # Get all soup descendants
    # Use .find_all()/.find()
    # Use .descendants
    # Use FOR LOOP iterate on all children
    # Use the ID attribute to get data
    print(divider(35))
    var = souper.find('li')

    def descendants(souper=None):
        descendants = var.descendants
        for child in descendants:
            print(f'\t {child}')
            # NavigableString
            if isinstance(child, bs4 \
                          .element \
                          .NavigableString):
                print(f'\t {child.string}')
    descendants()
    print(divider(35))
    print('\n')

    # Get the NEXT or PREVIOUS element
    # Use .next_element/.previous_element
    # Previous element is None
    print(divider(35))
    var = souper.find(attrs={'id': 'menu-item-31890'})
    print(var)
    print(divider(35))
    print(var.next_element)
    print(divider(35))
    print(var.previous_element)

    # Get the NEXT or PREVIOUS element
    # Use .next_element/.previous_element
    # Previous element is None
    print(divider(35))
    var = souper.find(attrs={'id': 'menu-item-31890'})
    print(var)
    print(divider(35))
    print(var.next_element)
    print(divider(35))
    print(var.previous_element)
    print(divider(35))
    print('\n')

    # Get all H1/H3/A
    # get with list parameter
    # Use .find_all([...])/.find([...])
    print(divider(35))
    print(souper.find_all(['h1', 'a']))
    print(divider(35))
    print(len(souper.find_all(['h1', 'a'])))
    print(divider(35))
    print('\n')

    # Get all contents
    # get with list parameter
    # Use .find_all([...])/.find([...])
    print(divider(35))
    var = souper.find_all(['h1', 'a'])
    def contents(varList: List):
        for item in var:
            if item.contents:
                print(item.contents)
    contents(var)
