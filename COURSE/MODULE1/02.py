#!/usr/bin/env python3
# Les DONNEES imbriquées (NESTED DATA)
# Les Dictionnaires


# PRE REQUIS
# ----------
# Imbriquer des données dans un dictionnaire
# Imbriquer des donnees sur plusieurs niveaux

# OBJECTIFS
# ---------
# Imbriquer des données dans les dictionnaires
# Comprendre l'importance des imbrications
# Evaluer la profondeur des imbrications de données


DATA = {
    'personal_data': {
        'name': 'Lauren',
        'age': 20,
        'major': 'Information Science',
        'physical_features': {
            'color': {
                'eye': 'blue',
                'hair': 'brown'
            },
            'height': '5.8',
        }
    },
    'other': {
        'favorite_colors': [
            'purple',
            'green',
            'blue'
        ],
        'interesting_in': [
            'social media',
            'intellectual property',
            'copyright',
            'music',
            'books',
        ]
    }
}


def divider(n=20):
    return '-'*n


if __name__ == '__main__':
    # Display DATA
    print(divider())
    print(DATA)
    print(type(DATA))
    print(DATA.get('personal_data', None))

    # Display a Color Item (1)
    print(divider())
    STEP1 = DATA['personal_data']
    print(divider())
    print(STEP1)
    print(type(STEP1))
    print(divider())
    STEP2 = STEP1['physical_features']
    print(STEP2)
    print(type(STEP2))
    print(divider())
    STEP3 = STEP2['color']
    print(STEP3)
    print(type(STEP3))

    # Display a Color Item (2)
    # We can do like that because
    # Each Element which is contain
    # In the NESTED ELEMENT is a Dict
    print(divider())
    COLOR = DATA['personal_data']['physical_features']['color']
    print(COLOR)

    # Display Favorite Colors
    # Display All Favorite Item
    print(divider())
    FAVORITE = DATA['other']['favorite_colors']
    print(FAVORITE)
    print(divider())
    print(FAVORITE[0])
    print(FAVORITE[1])
    print(FAVORITE[2])

    # Test All Results
    assert FAVORITE[0] == 'purple'
    assert FAVORITE[1] == 'green'
    assert FAVORITE[2] == 'blue'
