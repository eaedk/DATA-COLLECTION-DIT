# 1- Le noeud name. On a le nom complet
# Séparateur Espace (' ')
# 2- Le noeud list.
# Séprateur Virgule (',')
# Fonction split qui permet de séparer
# Cette fonction nous renvoie une liste
# -------------------------------------
# FullName = Nom + Prénom
# Liste en python [item1, item2, item3]
# Mettre un nom (FULLNAME)
# Liste en python
# -------------------------------------
# open()
# 	- filepath
# 	- action/MODE (Read/Write/Append)

import json
from typing import List


def readFile(filename: str):
    with open(filename, 'r') as file:
        data = file.read()
        file.close()
    return data


def deserialize(data: str):
    return json.loads(data)


def modifyPayload(data: List[dict]):
    def construct(item: dict):
        if item.get('name') != None:
            splitter = item \
                .get('name') \
                .split(' ')
            item['name'] = {
                'lastName': splitter[0].upper(),
                'firstName': splitter[-1].capitalize(),
            }
        return item
    return list(map(construct, data))


def modifyPayload2(data: List[dict]):
    def construct(item: dict):
        if item.get('list') != None:
            splitter = item \
                .get('list') \
                .split(', ')
            item['list'] = splitter
        return item
    return list(map(construct, data))


# Avoir un nouveau noeud
# Ayant comme key (personal_data)
# 	- Ayant comme value (dict)
# 		- guid
# 		- firstName
# 		- lastName
# 		- phone
# 		- country
def modifyPayload3(data: List[dict]):
    pass


# Avoir un nouveau noeud
# Ayant comme key (bank_data)
# 	- Ayant comme value (dict)
# 		- pan
# 		- pin
# 		- cvv
# 		- iban
# 		- currency
def modifyPayload4(data: List[dict]):
    pass


# Avoir un nouveau noeud
# Ayant comme key (activities)
# Ayant comme valeur le contenu du noeud list
def modifyPayload5(data: List[dict]):
    pass


# Supprimer les noeuds
# 	- name
# 	- country
# 	- pan
# 	- iban
# 	- pin
# 	- cvv
# 	- currency
# 	- guid
# 	- phone
# 	- list
def modifyPayload6(data: List[dict]):
    pass


if __name__ == '__main__':
    data = readFile('../MODULE1/TPMODULE1/DATABASES/file.json')
    data = deserialize(data)
    data = modifyPayload(data)
    data = modifyPayload2(data)
    print(data[:2])
