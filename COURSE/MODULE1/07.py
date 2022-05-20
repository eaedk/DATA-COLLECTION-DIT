#!/usr/bin/env python3
# Deep and Shallow Copies
# Deep Copies (Copie profonde)

import copy

ORIGINAL = [
    ['dogs', 'puppies'],
    ['cats', 'kittens']
]

ORIGINAL2 = [
    ['canines', ['dogs', 'puppies']],
    ['felines', ['cats', 'kittens']],
]


def divider(n=20):
    """Summary

    Args:
        n (int, optional): Description

    Returns:
        TYPE: Description
    """
    return '-'*n


if __name__ == '__main__':
    # Print ORIGINAL List
    
    ORIGINAL = [
        ['dogs', 'puppies'],
        ['cats', 'kittens']
    ]

    ORIGINAL2 = [
        ['canines', ['dogs', 'puppies']],
        ['felines', ['cats', 'kittens']],
    ]

    # Deep Copy with first Way
    COPIED_OUTER_LIST = []
    for INNER_LIST in ORIGINAL:
        COPIED_INNER_LIST = []
        for item in INNER_LIST:
            COPIED_INNER_LIST.append(item)
        COPIED_OUTER_LIST.append(COPIED_INNER_LIST)

    # Now print the COPIED OUTER LIST
    # After compare two lists
    print(divider())
    print(COPIED_OUTER_LIST)
    print(divider())
    print(ORIGINAL is COPIED_OUTER_LIST)
    print(divider())
    print(ORIGINAL == COPIED_OUTER_LIST)

    # Add some Value in Original first Element
    # Use Append and Index technic
    ORIGINAL[0].append(['canines'])
    print(divider())
    print(ORIGINAL)
    print(divider())
    print('Look at now the COPIED VESRION')
    print(COPIED_OUTER_LIST)

    # Compare two both list
    # With Is we have False
    # With == we have False Too
    # Conclusion a Deep copy dont take
    # A ORIGINAL memory address
    print(divider())
    print(ORIGINAL is COPIED_OUTER_LIST)
    print(divider())
    print(ORIGINAL == COPIED_OUTER_LIST)

    # Deep Copy with Second Way
    # Use a List Slice property
    print(divider())
    ORIGINAL = [
        ['dogs', 'puppies'],
        ['cats', 'kittens']
    ]
    COPIED_OUTER_LIST = []
    for INNER_LIST in ORIGINAL:
        COPIED_INNER_LIST = INNER_LIST[:]
        COPIED_OUTER_LIST.append(COPIED_INNER_LIST)
    print(COPIED_OUTER_LIST)

    # Use Copy Module
    # Use a SHALLOW Copy method With Slice Property
    # Shallow Copy use the List memory address
    # Deep copy here dont use a memory address
    # With copy.deepcopy(x)
    print('\n')
    print(divider())
    SHALLOW_COPY_VERSION = ORIGINAL2[:]
    DEEP_COPY_VERSION = copy.deepcopy(ORIGINAL2)
    ORIGINAL2.append('Hi there')
    ORIGINAL2[0].append(['marsupials'])
    print('---------- Original -----------')
    print(ORIGINAL2)
    print('---------- Depp Copy -----------')
    print(DEEP_COPY_VERSION)
    print('---------- Shallow Copy -----------')
    print(SHALLOW_COPY_VERSION)
