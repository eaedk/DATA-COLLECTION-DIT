#!/usr/bin/env python3
# Structure Nested Data
# Structuration des données Imbriquées

NESTED = [
    1,
    2,
    ['a', 'b', 'c'],
    ['d', 'e'],
    ['f', 'g', 'h']
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
    # print NESTED List
    print(divider())
    print(NESTED)
    print('\n')

    for item in NESTED:
        print('Level1: ')
        if isinstance(item, list):
            for subitem in item:
                print('\tLevel2: {}'.format(subitem))
        else:
            print(item)
