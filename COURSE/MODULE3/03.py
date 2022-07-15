# Web Scrapping
# https://beautiful-soup-4.readthedocs.io/en/latest/
# https://docs.python.org/3/library/time.html
import re
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://history.state.gov'


class ScrapFactory(object):
    @classmethod
    def fetch(cls, url: str):
        with requests.Session() as session:
            data = session.get(url)
        return data.text

    @classmethod
    def setBs4Instance(cls, url: str):
        data = BeautifulSoup(
            cls.fetch(url),
            features="html.parser"
        )
        return data

    @classmethod
    def cleanByReplace(cls, string: str):
        string = str(string)
        regex = re.compile('/countries/\w+')
        string = re.findall(regex, string)
        return string[0]

    @classmethod
    def formUrlLink(cls, string: str):
        return f'{BASE_URL}{string}'

    @classmethod
    def getLinkList(cls, SoupList: list):
        return [
            cls.formUrlLink(
                cls.cleanByReplace(link))
            for link in SoupList
        ]

    @classmethod
    def getImgLink(cls, instanceBs4):
        return instanceBs4.find(class_='tei-graphic')['src']

    @classmethod
    def scrapChildLinkList(cls, SoupUrlList: list):
        newList = []
        for link in SoupUrlList:
            data = cls.setBs4Instance(link)
            data = data.find(class_='tei-graphic')
            if data:
                newList.append(data['src'])
            continue
        return newList



if __name__ == '__main__':
    data = BeautifulSoup(
        ScrapFactory.fetch('https://history.state.gov/countries/all'),
        features="html.parser"
    )

    # Recupérer pour tous les liens
    # De chaque pays l'URL de l'image du drapeau du pays
    # Mettre ces informations dans une liste
    #   Cette liste doit contenir des tuple
    #   Chaque dictionnaire doit contenir
    #       key (Name) Value => Le nom du pays scrappé
    #       key (Url) Value => L'URL du pays
    #       key (Image) Value => L'URL de l'image du pays
    #       key (Persons) Value => [
    #           key (Name) Value => Nom,
    #           key (Url) Value => Url qui renvoie sur la page de la personne
    #       ]

    # data.find(class_='tei-graphic') # 1
    # data.find_all(class_='tei-graphic') # [1]

    regex = re.compile('/countries/\w+')
    lista = data.find_all(href=regex)
    lista = lista[2:-1]

    instance = ScrapFactory
    childUrl = instance.getLinkList(lista)

    var1 = instance.setBs4Instance(childUrl[0])
    imgLogo = var1.find(class_='tei-graphic')
    imgLogoSrc = imgLogo['src']
    print(imgLogoSrc)
