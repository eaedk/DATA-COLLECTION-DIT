#!/usr/bin/env python3
# Iteration des elements imbriqués
# Technique de l'Iteration des Elements Imbriqués
# Utilisation du Pattern d'accumulation

# PRE REQUIS
# ----------
# Connaitre les Boubles en python
# Avoir la maitrise fes utilitaires de parcours de liste
# Maitriser les structures conditionnelles

# OBJECTIFS
# ---------
# Parcourir les données imbriquées
# Avoir le reflexe de l'optimiosation des parcours
# Maitriser l'utulisation de la fonction enumerate
# Reduire le cout des instructions de parcours avec la bonne approche
# Maitriser la technique de l'ITERATION
# Maitriser la technique de l'ACCUMULATION

NESTED = [
    [1, 2],
    [3, 4],
    [5, 6],
]

NESTED1 = [
    ['Tina', 'Turner', 1939, 'Singer'],
    ['Matt', 'Domon', 1970, 'Actor'],
    ['Kristen', 'Wiig', 1973, 'Comedian'],
    ['Michael', 'Saveur', 1939, 'Footballer'],
]

NESTED2 = [
    [
        'apples',
        'bananas',
        'oranges',
        'blueberries',
        'lemons',
    ],
    [
        'carrots',
        'peas',
        'cucumbers',
        'green beans',
    ],
    [
        'root beer',
        'smoothies',
        'cranberry juice',
        'kiwis',
    ],
]


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    NESTED = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    # print NESTED List
    print(divider())
    print(NESTED)
    print('\n')

    print(divider())
    for item in NESTED:
        print('Level1: ')
        for subitem in item:
            print('\tLevel2: {}'.format(subitem))

    print(divider())
    # Print Every Person Last Name
    # Use Enumerate And Index Table notion
    # One way do print the result (1)
    for person in NESTED1:
        for index, item in enumerate(person):
            if index == 1:
                print(item)

    # Print Every Person Last Name
    # Use Enumerate And Index Table notion
    # One way do print the result (2)
    print(divider())
    for person in NESTED1:
        if isinstance(person, list):
            print(person[1])

    # Create a new list to accumulate LastName
    # Use Second Way to append LastName on LIST
    # Use Global Variable: LASTNAME
    LASTNAME = []
    print(divider())
    for person in NESTED1:
        if isinstance(person, list):
            LASTNAME.append(person[1])
    print(LASTNAME)

    # Utilisons la technique de l'iteration
    # Des Elements imbriquées pour retrouver
    # Les Elements commençont par "B"
    B_LIST = []
    print(divider())
    for item in NESTED2:
        for subitem in item:
            if any([
                'b' in subitem,
                'B' in subitem
            ]):
                B_LIST.append(subitem)
    print(B_LIST)

    for item in NESTED1:
        print(item[0])
