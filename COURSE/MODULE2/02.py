#!/usr/bin/env python3
# Liste compréhension
import json


def divider(n=20) -> str:
    """Summary

    Parameters
    ----------
    n : int, optional
        Description

    Returns
    -------
    str
        Description
    """
    return '-' * n


def flatListe(Liste: list) -> list:
    """Summary

    Parameters
    ----------
    Liste : list
        Description

    Returns
    -------
    list
        Description
    """
    return sorted([
        item
        for subitem in Liste
        for item in subitem
    ])


def keepEvens(nums: list) -> list:
    """Summary

    Parameters
    ----------
    nums : list
        Description

    Returns
    -------
    list
        Description
    """
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


def keepEvens2(nums: list) -> list:
    """Summary

    Parameters
    ----------
    nums : list
        Description

    Returns
    -------
    list
        Description
    """
    new_list = [num for num in nums if num % 2 != 0]
    return new_list


def keepEvens3(nums: list) -> list:
    """Summary

    Parameters
    ----------
    nums : list
        Description

    Returns
    -------
    list
        Description
    """
    new_list = filter(lambda num: num % 2 == 0, nums)
    return list(new_list)


if __name__ == '__main__':
    # Generate Listes
    # Liste1, Liste2, Liste3, Liste4, Liste5
    Liste1 = [2, 4, 8, 10, 12, 14, 16, 18, 20]
    Liste2 = [1, 3, 5, 9, 11, 13, 15, 17, 19]

    # Use range(start, final, interval)
    # generate couples of number with range
    # Apply liste compréhension syntaxe
    Liste3 = [x for x in range(10)]
    Liste4 = [x for x in range(2, 21, 2)]
    Liste5 = [x for x in range(1, 20, 2)]

    # Display All Listes
    # Use liste compréhension for Liste3
    # Use liste compréhension for Liste4
    # Use liste compréhension for Liste5
    print(divider())
    print(Liste1)
    print(divider())
    print(Liste2)
    print(divider())
    print(Liste3)
    print(divider())
    print(Liste4)
    print('\n')

    # Use a function keepEvens
    # Use liste compréhension for filtering
    # Use zip to make new Liste
    print(divider())
    Liste = list(zip(Liste1, Liste2))
    Liste = flatListe(Liste)
    print(Liste)
    Liste1 = keepEvens(Liste)
    print(Liste1)
    print(divider())
    Liste2 = keepEvens2(Liste)
    print(Liste2)
    print(divider())
    Liste3 = keepEvens3(Liste)
    print(Liste3)
    print('\n')

    # Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester.
    # Do this using a list comprehension.
    tester = {
        'info': [
            {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
            {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
            {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
            {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
            {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
            {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}
        ]
    }
    print(divider())
    tester = {'info': [item['name'] for item in tester['info']]}
    print(tester)
    print('\n')

    # Do this using a list comprehension.
    # Prettify the testser output
    print(divider())
    print(json.dumps(tester, indent=4))
    print('\n')

    # Extract the name List out tester
    print(divider())
    print(tester['info'])
    print('\n')

    # Wirte a function longlengths
    # This function should return the length of thoses strings at least 4 characters
    # Fisrt Solution (1)
    def longlengths(strings):
        return [len(value) for value in strings if len(value) >= 4]

    print(divider())
    Liste = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
    print(longlengths(Liste))
    print('\n')

    # Wirte a function longlengths
    # This function should return the length of thoses strings at least 4 characters
    # Second Solution (2)
    def longlengths(strings):
        accum = []
        for s in strings:
            if len(s) >= 4:
                accum.append(len(s))
        return accum

    print(divider())
    print(longlengths(Liste))
    print('\n')

    # Wirte a function longlengths
    # This function should return the length of thoses strings at least 4 characters
    # Third Solution (3)
    def longlengths(strings):
        filtering = filter(lambda s: len(s) >= 4, strings)
        return list(map(lambda s: len(s), filtering))

    print(divider())
    print(longlengths(Liste))
