#!/usr/bin/env python3
# Extractionn from Nested Data
# Extraction des données depuis des données imbriqués

import json
from collections import Counter


ORIGINAL = [
    [
        ['one', 'two'],
        ['seven', 'eight']
    ],
    [
        ['nine', 'four'],
        ['three', 'one']
    ],
    [
        ['two', 'eight'],
        ['seven', 'four']
    ],
    [
        ['five', 'one'],
        ['four', 'two']
    ],
    [
        ['six', 'eight'],
        ['two', 'seven']
    ],
    [
        ['three', 'five'],
        ['one', 'six']
    ],
    [
        ['nine', 'eight'],
        ['five', 'four']
    ],
    [
        ['six', 'three'],
        ['four', 'seven']
    ]
]


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    # Count Word in the ORIGINAL data
    # Take each word and set it like Dict Key
    # And put the Count of this word to Value
    # First Way to resolve this problematic
    print(divider())
    WORD_COUNT = {}
    for item in ORIGINAL:
        for subitem in item:
            for word in subitem:
                if word in WORD_COUNT:
                    WORD_COUNT[word] += 1
                else:
                    WORD_COUNT[word] = 1
    print(WORD_COUNT)

    # Count Word in the ORIGINAL data
    # Take each word and set it like Dict Key
    # And put the Count of this word to Value
    # First Way to resolve this problematic
    FLAT_LIST = []
    for item in ORIGINAL:
        for subitem in item:
            FLAT_LIST.append(subitem[0])
            FLAT_LIST.append(subitem[1])

    # Use Counter Collection to count
    # Use Sorted Method to order by ASC
    print(divider())
    COUNTER_FLAT_LIST = Counter(FLAT_LIST)
    COUNTER_FLAT_LIST = dict(COUNTER_FLAT_LIST)
    print(COUNTER_FLAT_LIST)
