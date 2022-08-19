# Installer requests dans votre ENV
# URL DOWNLOAD (https://pypi.org/project/requests/)
# URL DOC (https://requests.readthedocs.io/en/latest/)
# URL formatter online (https://jsonformatter.curiousconcept.com/)
import requests

# URL = 'https://restcountries.com/v2/all'
URL2 = 'https://restcountries.com/v2/name/{name}'
URL3 = 'https://api.datamuse.com/words'


# Formattage de string
# --------------------
# name = Afghanistan
# URL2 = 'https://restcountries.com/v2/name/{0}'.format(name)
# URL2 = 'https://restcountries.com/v2/name/{}'.format(name)
# URL2 = f'https://restcountries.com/v2/name/{name}'
# URL2 = 'https://restcountries.com/v2/name/' params={'name': ...}


if __name__ == '__main__':
    # r = requests.get(URL)
    # print(r.status_code)
    # headers['content-type']
    # Dictionnaires
    # key/Value
    # print(headers)
    # print(r.headers)
    # print(r.headers['content-type'])
    # print(r.json())
    # print('\n')

    # Paramètres
    # https://www.youtube.com/watch?v=UUga4-z7b6s
    # PROTOCOLE (HTTP)
    # DNS (youtube.com)
    # CNAME (www)
    # path URL (watch)
    # PARAMS (?{key}={value})
    # Dictionnaire (key:value)
    # {key:value} <==> key=value <==> **kwargs
    name = 'Afghanistan'
    # URL2 = 'https://restcountries.com/v2/name/{0}'.format(name)
    # URL2 = 'https://restcountries.com/v2/name/{}'.format(name)
    # URL2 = f'https://restcountries.com/v2/name/{name}'
    # URL2 = f'https://restcountries.com/v2/name/?name={name}'

    r = requests.get(URL3, params={'sl': 'jirraf'})
    print(r.status_code)
    # print(r.json())
    print('\n')

    payload = {'sl': 'jirraf'}
    r = requests.get(URL3, params=payload)
    print(r.status_code)
    # print(r.json())
    print('\n')

    # /words?ml=breakfast&rel_rhy=grape
    payload = {'ml': 'breakfast', 'rel_rhy': 'grape'}
    r = requests.get(URL3, params=payload)
    print(r.status_code)
    # print(r.json())
    print('\n')
