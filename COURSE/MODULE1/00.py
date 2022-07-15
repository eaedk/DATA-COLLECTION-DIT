#!/usr/bin/env python3
# Les LISTES et les DICTIONNAIRES
# L'utilisation des Listes et des Dictionnaires


# PRE REQUIS
# ----------
# La manipulation des LISTES
# La manipulation des DICTIONNAIRES
# Utilisation des fonctions de bases
# Manipulation des données imbriquées

# OBJECTIFS
# ---------
# Manipuler les listes
# Ajouter dans une liste
# Manipuler les dictionnaires
# Ajouter dans un dictionnaire


LISTE1, LISTE2 = [], list()
DICT1, DICT2 = {}, dict()


LISTE1.append(LISTE2)  # [[]]

LISTE1.append(DICT1)  # [[], {}]


LISTE1[0] = DICT1  # [{}, {}]


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    # Display LISTE1, LIST2
    print(divider())
    print(LISTE1, LISTE2)

    # Display DICT1, DICT2
    print(DICT1, DICT2)
    print(divider())

    # Add DATA in LIST1, LIST2
    LISTE1.append(12.1772)
    LISTE2.append(DICT1)
    LISTE2.append(DICT2)
    LISTE2.append('DIT: Master1')
    LISTE2.append(14.)
    LISTE1.append(LISTE2)

    print(LISTE1)
    print(divider())
    print(LISTE2)
    print(divider())
    LISTE1.append([x for x in range(33, 39)])
    print(LISTE1)
    print(divider())
    print(LISTE2)
    print(divider())

    # Add DATA in DICT1, DICT2
    DICT1['name'] = 'DIT'
    DICT1['grade'] = 'Master1'
    DICT1['year'] = 2022
    DICT1['data2'] = DICT2
    DICT2['price'] = 285000.98
    DICT2['period'] = '2022-01-01'
    DICT1['data2'] = DICT2
    print(DICT1['data2'])

    print(LISTE1)
    print(LISTE2)
