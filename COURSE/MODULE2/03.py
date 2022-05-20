#!/usr/bin/env python3
# Liste compréhension
# Zip Function


def divider(n=20):
    return '-' * n


Liste1 = [3, 4, 5]
Liste2 = [1, 2, 3]
Liste3 = []


if __name__ == '__main__':
    # Display All Listes
    print(divider())
    print(Liste1)
    print(Liste2)
    print('\n')

    # Add of two Lists
    for i in range(0, len(Liste1)):
        Liste3.append(Liste1[i] + Liste2[i])
    print(divider())
    print(Liste3)
    print('\n')

    # Use Zip function
    # Use Class list to cast a generator
    # Using of Zip return a generator
    print(divider())
    Liste4 = zip(Liste2, Liste1)
    Liste4 = list(Liste4)
    print(Liste4)

    # Override Liste3
    # Affect Empty List for List3
    # Method 1
    Liste3 = []
    for item in Liste4:
        Liste3.append(item[0] + item[1])
    print(divider())
    print(Liste3)
    print('\n')

    # Override Liste3
    # Affect Empty List for List3
    # Method 2 (Unpack tuple)
    Liste3 = []
    for (x1, x2) in Liste4:
        Liste3.append(x1 + x2)
    print(divider())
    print(Liste3)
    print('\n')

    # Override Liste3
    # Affect Empty List for List3
    # Method 3 (Unpack tuple & List Compréhension)
    Liste3 = [x1+x2 for (x1, x2) in Liste4]
    print(divider())
    print(Liste3)
    print('\n')
