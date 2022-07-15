#!/usr/bin/env python3
# Structure Nested Data
# Structuration des données Imbriquées


# PRE REQUIS
# ----------
# Connaitre les Boubles en python
# Avoir la maitrise fes utilitaires de parcours de liste
# Maitriser les structures conditionnelles

# OBJECTIFS
# ---------
# Savoir structurer les donnés imbriquées
# Détecter les niveaux d'imbrications


NESTED = [
    1,
    2,
    ['a', 'b', 'c'],
    ['d', 'e'],
    ['f', 'g', 'h']
]


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    # print NESTED List
    print(divider())
    print(NESTED)
    print('\n')

    # Afficher les niveaux
    # Imbrications de la donnée NESTED
    for item in NESTED:
        print('Level1: ')
        if isinstance(item, list):
            for subitem in item:
                print('\tLevel2: {}'.format(subitem))
        else:
            print(item)
