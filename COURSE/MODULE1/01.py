#!/usr/bin/env python3
# Les DONNEES imbriquées (NESTED DATA)
# Les Listes

# PRE REQUIS
# ----------
# Imbriquer des données dans une liste
# Imbriquer des donnees sur plusieurs niveaux

# OBJECTIFS
# ---------
# Imbriquer des données dans les listes
# Comprendre l'importance des imbrications
# Evaluer la profondeur des imbrications de données


NESTED1 = [
    ['a', 'b', 'c'],
    ['d', 'e'],
    ['f', 'g', 'h']
]

print(NESTED1[0][1])

DATA = [
    ['Yassa', 'Bissap', 'Banane'],
    [34, 69, 88, []],
    [['willow', ['birch', 'Rice'], 'elm'], 'apple'],
    ['Banana', 'Orange', 'Garlic', 'Tomato'],
]


A = [1, 2, 3, 4]

[x for x in A if x % 2 == 0]


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    # Display NESTED1 Element (1)
    print(divider())
    print(NESTED1)
    print(divider())
    print(len(NESTED1))
    print(divider())
    print(NESTED1[0])
    print(divider())
    print(NESTED1[1])
    print(divider())
    print(NESTED1[2])
    NESTED1.append(['i'])

    # Display NESTED1 Element (2)
    print('\n')
    print(divider())
    for item in NESTED1:
        print(item)

    # Display NESTED1 Element type
    # If you have List in Parent List
    # You can Apply all function of List
    # In all child List called Nested List
    print('\n')
    print(divider())
    for item in NESTED1:
        print(type(item))

    # Get and Modify Nested List
    # We do this Example with NESTED1
    print('\n')
    print(divider())
    NESTED1[0].append(00)
    NESTED1[1].append({'0': 0, '1': 1})
    NESTED1[2].append((1, 2, 3, 4, 5))
    NESTED1[3] = ['i', 'j']
    print(NESTED1)

    # Display NESTED1 lenght
    print('\n')
    print(divider())
    print(len(NESTED1))

    # Displayb DATA nested Value
    # Display Willow Value
    WILLOW = DATA[2][0][0]
    assert WILLOW == 'willow'

    # Displayb DATA nested Value
    # Display Rice Value
    print(divider())
    RICE = DATA[2][0][1][1]
    assert RICE == 'Rice'
