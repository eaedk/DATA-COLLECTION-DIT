#!/usr/bin/env python3
# Deep and Shallow Copies
# Shallow Copies (Copie peu profonde)

ORIGINAL = [
    ['dogs', 'puppies'],
    ['cats', 'kittens']
]

COPIED_VESRION = ORIGINAL[:]
COPIED_VESRION2 = ORIGINAL.copy()


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    # Print ORIGINAL List
    print(divider())
    print(ORIGINAL)

    # Print COPIED VESRION List
    # Check if two List are equal
    # L'operateur de comparaison is (False)
    # L'operateur de comparaison == (True)
    print(divider())
    print(COPIED_VESRION)
    print(divider())
    print(ORIGINAL is COPIED_VESRION)
    print(divider())
    print(ORIGINAL == COPIED_VESRION)

    # Second comparaison
    # Use the Copy Method Case
    print(divider())
    print(ORIGINAL is COPIED_VESRION2)
    print(divider())
    print(ORIGINAL == COPIED_VESRION2)

    # ADD Some value in ORIGINAL List
    # Use Append List Method
    print(divider())
    ORIGINAL[0].append(['canines'])
    print(ORIGINAL)
    print(divider())
    print('Look at now the COPIED VESRION')
    print(COPIED_VESRION)

    COPIED_VESRION[0].append(['molaires'])

    print('\n')
    print(ORIGINAL)
    print(COPIED_VESRION)
    print(COPIED_VESRION2)
