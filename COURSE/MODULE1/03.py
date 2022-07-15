#!/usr/bin/env python3
# Utilisation du module JSON

# PRE REQUIS
# ----------
# Connaitre la structure KEY-VALUE
# Manipuler les dictionnaires
# Connaitre le JSON format
# Importation des modules nécessaire
# Connaissance breve du module JSON de python

# OBJECTIFS
# ---------
# Importer le module JSON
# Manipuler les fonctions du module JSON
# Parser les données
# Reconstruire le type initial de la donnée
# Serialiser et désérialiser


import json

DATA = '\n\n\n{\n "resultCount": 25,\n "results": [\n{"wrapperType": "track", "kind": "podcast", "collectionId": 10892}]}'


def divider(n=20):
    return '-'*n


def pretty(obj={},
           sort_keys=True,
           indent=2):
    return json.dumps(
        obj,
        sort_keys=sort_keys,
        indent=indent
    )


if __name__ == '__main__':
    # Load DATA with JSON
    # Use Module to get Dict
    print(divider())
    LOADER = json.loads(DATA)
    print(LOADER)
    print(type(LOADER))

    # Load DATA with JSON
    # print Dict keys
    print(divider())
    print(list(LOADER.keys()))

    # Load DATA with JSON
    # print Dict values
    print(divider())
    print(LOADER.values())

    # Load DATA with JSON
    # print Dict items
    print(divider())
    print(LOADER.items())

    # Load DATA with JSON
    # print LOADER resultCount value
    # print LOADER result value
    print(divider())
    print(LOADER.get('resultCount'))
    print(LOADER.get('results'))

    # Load pretty way
    print(divider())
    print(pretty(LOADER))

    # Load pretty way
    print(divider())
    print(pretty(LOADER, indent=4))
