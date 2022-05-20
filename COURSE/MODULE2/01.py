#!/usr/bin/env python3
# Map and Filter Module
# Filter Module
import math


# Generate Liste
Liste = [x for x in range(10)]


def divider(n=20):
    return '-' * n


def f(x): return x % 2 == 0
def g(x): return x % 2 != 0
def h(x): return x > 2
def i(x): return x < 2


def keepEvens(nums: list):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


def keepEvens2(nums: list):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)


if __name__ == '__main__':
    # Apply a filter function
    # Use a lambda function expression
    Listef = list(filter(f, Liste))
    Listeg = list(filter(g, Liste))
    Listeh = list(filter(h, Liste))
    Listei = list(filter(i, Liste))

    # Display all filtering list
    divider()
    print(Listef)
    divider()
    print(Listeg)
    divider()
    print(Listeh)
    divider()
    print(Listei)
    print('\n')

    # Apply keepEvens function
    # Get all value that module equal 0
    print(divider())
    numbers = [3, 4, 6, 7, 0, 1]
    print(numbers)
    print(divider())
    numbers = keepEvens(numbers)
    print(numbers)

    # Apply keepEvens2 function
    # Get all value that module equal 0
    print(divider())
    numbers = [3, 4, 6, 7, 0, 1]
    numbers = keepEvens2(numbers)
    print(numbers)
    print('\n')

    # Get all values that only contains "O"
    print(divider())
    lst = ['witch', 'halloween', 'pumpkin', 'cat', 'candy', 'wagon', 'moon']
    lst2 = filter(lambda value: ("o" in value or "O" in value), lst)
    print(lst)
    print(divider())
    print(list(lst2))
