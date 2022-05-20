#!/usr/bin/env python3
# Map and Filter Module
# Map Module
import math


def divider(n=20):
    return '-' * n


def doubleStuff(a_list: list):
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list


def triple(value):
    return 3 * value


def quadrupleStuff(a_list: list):
    new_list = map(lambda value: 4*value, a_list)
    return new_list


def tripleStuff(a_list: list):
    new_list = map(triple, a_list)
    return new_list


if __name__ == '__main__':
    # Apply doubleStuff function
    print(divider())
    things = [2, 5, 9]
    print(things)
    print(divider())
    things = doubleStuff(things)
    print(things)
    print('\n')

    # Apply tripleStuff function
    # Apply quadrupleStuff function
    print(divider())
    things3 = tripleStuff(things)
    print(list(things3))
    print(divider())
    things4 = quadrupleStuff(things)
    print(list(things4))
    print('\n')

    # Apply map function
    print(divider())
    abbreves = ['usa','esp','chn','jpn','mex','can','rus','rsa','jam', ]
    abbreves_upper = map(lambda x: x.upper(),abbreves)
    print(abbreves)
    print(divider())
    print(list(abbreves_upper))

    # Apply a Slice property to take 2 first letter
    # Apply a Slice property to take 1 first letter
    print(divider())
    abbreves_upper = map(lambda x: x[:2].upper(),abbreves)
    print(list(abbreves_upper))
    print(divider())
    abbreves_upper = map(lambda x: x[:1].upper(),abbreves)
    print(list(abbreves_upper))
