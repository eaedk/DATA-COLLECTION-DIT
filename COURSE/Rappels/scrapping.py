import bs4
import requests
from bs4 import BeautifulSoup

URL = 'https://dit.sn/'


def divider(n=35):
    return '-' * n


def httpFetcher(URL: str,
                params=None,
                headers=None):
    result = requests.get(URL,
                          params=params,
                          headers=headers)
    result = result.text
    return result


if __name__ == '__main__':
    result = httpFetcher(URL)
    souper = BeautifulSoup(
        result,
        'html.parser')
    # <class 'bs4.BeautifulSoup'>
    print(divider())
    print(type(souper))
    print('\n')

    # Récupération des élements du DOM
    # Récupération des balises h1
    # Utilisation de find_all()
    print(divider())
    print(souper.find_all('h1'))
    print(divider())
    print('\n')

    # Récupération des élements du DOM
    # Récupération des balises link
    # Utilisation de find_all()
    print(divider())
    print(souper.find_all('link'))
    print(divider())
    print(len(souper.find_all('link')))
    print(divider())
    # <class 'bs4.element.ResultSet'>
    # Qui hérite de la classe list...
    # Retourne une liste
    print(type(souper.find_all('link')))
    print(divider())
    print('\n')

    # Récupération des élements du DOM
    # Récupération des balises h2
    # Utilisation de find()
    # Retourne le premier élément trouvé
    print(divider())
    print(souper.find('h2'))
    print(divider())
    print(souper.find_all('h2'))
    print(divider())
    print('\n')

    # Récupération des élements du DOM
    # Récupération par l'identifiant (id)
    # id est un attribut de la balise
    # Utilisation de find_all()/find()
    # Retourne le premier élément trouvé
    print(divider())
    print(souper.find(id='menu-item-31890'))
    print(souper.find(id='menu-item-28943'))
    print(souper.find(id='menu-item-30993'))
    print(souper.find(id='menu-item-28969'))
    print(divider())
    print('\n')

    # Récupération des élements du DOM
    # Récupération par l'identifiant (id)
    # id est un attribut de la balise
    # Utilisation de find_all()/find()
    # Utilisation de attrs
    print(divider())
    print(souper.find(attrs={'id': 'menu-item-31890'}))
    print(souper.find(attrs={'id': 'menu-item-28943'}))
    print(divider())
    print('\n')

    # Récupération des élements du DOM
    # Récupération par la (class)
    # id est un attribut de la balise
    # Utilisation de find_all()/find()
    # Utilisation de attrs
    print(divider())
    print(souper.find(attrs={'class': 'menu-item'}))
    print(souper.find(attrs={'class': 'menu-item'}))
    print(divider())
    print('\n')

    # Récupérer le contenu
    # Utiliser contents
    # Pour récupérer le contenu d'un élément
    var = souper.find(attrs={'id': 'menu-item-31890'})
    print(divider())
    print(var.contents)
    print('\n')

    # Récupérer le parent
    # Utiliser .parent
    # Pour récupérer le contenu d'un élément
    var = souper.find(attrs={'id': 'menu-item-31890'})
    print(divider())
    print(var.parent)
    print('\n')

    # Récupérer en passant une liste en parametre
    # Utiliser de find_all([....])
    # Récupérer les h2 & a & li
    print(divider())
    print(souper.find_all(['h2', 'a', 'li']))
    print(divider())
    print('\n')

    # Récupérer le contenu des attributs
    # afficher le type des éléments
    # Utiliser la syntaxe des dictionnaire
    # ['NOM DE LA KEY']
    print(divider())
    # <class 'bs4.element.Tag'>
    var = souper.find_all('a')[0]
    print(type(var))
    print(divider())
    print(var['href'])
    print('\n')
