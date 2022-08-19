# Introduction à pandas

import random

import pandas as pd

BASE_URL = 'COURSE/DATABASES/data-_zJ9Zko2Dh1LYlNNgALKE.csv'


class Utils(object):
    @classmethod
    def divider(cls, n=54):
        return '-' * n

    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x


if __name__ == '__main__':
    # Ouvrir un fichier CSV
    data = pd.read_csv(
        BASE_URL,
        encoding='utf-8')
    print(Utils.divider())
    print(data.head())
    print('\n')

    # Afficher les 5 premières lignes
    # Utlisation de la fonction .head()
    print(Utils.divider())
    print(data.head())
    print('\n')

    # Afficher les 10 premières lignes
    # Utlisation de la fonction .head()
    print(Utils.divider())
    print(data.head(10))
    print('\n')

    # Afficher les 5 dernières lignes
    # Utlisation de la fonction .tail()
    print(Utils.divider())
    print(data.tail())
    print('\n')

    # Afficher les 10 dernières lignes
    # Utlisation de la fonction .tail()
    print(Utils.divider())
    print(data.tail(10))
    print('\n')

    # Afficher les colonnes
    print(Utils.divider())
    print(data.columns)
    print(list(data.columns))
    print('\n')

    # Afficher les dimensions
    # Affichier Nombre colonne
    # Afficher Nombre de ligne
    print(Utils.divider())
    print(data.shape)
    print(f'NL: {data.shape[0]}')
    print(f'NC: {data.shape[1]}')
    print('\n')

    # Afficher une colonne
    # Première approche
    # Exemple: colonne NAME
    print(Utils.divider())
    print(data['name'])
    print('\n')

    # Afficher une colonne
    # Première approche
    # Exemple: colonne EMAIL
    print(Utils.divider())
    print(data['email'])
    print('\n')

    # Afficher une colonne
    # Deuxième approche
    # Exemple: colonne NAME
    print(Utils.divider())
    print(data.name)
    print('\n')

    # Afficher une colonne
    # Deuxième approche
    # Exemple: colonne EMAIL
    print(Utils.divider())
    print(data.email)
    print('\n')

    # Afficher la première ligne
    # SALLAH DIA purpose
    print(Utils.divider())
    print(data.head(1))
    print('\n')

    # Afficher la première ligne
    # AFI purpose
    print(Utils.divider())
    print(data.iloc[0])
    print('\n')

    # Afficher la première ligne
    print(Utils.divider())
    print(data.loc[0])
    print('\n')

    # Afficher la première ligne
    # LANDRY bete purpose
    print(Utils.divider())
    print(data.loc[[0]])
    print('\n')

    # Afficher la première ligne
    # Mamadou Kebe bete purpose
    print(Utils.divider())
    print(data.iloc[:1])
    print('\n')

    # Afficher les deux premières
    # Colonnes uniquement
    # Première approche
    print(Utils.divider())
    print(data.iloc[:, [0, 2]])
    print('\n')

    # Afficher les deux premières
    # Colonnes uniquement
    # Deuxième approche approche
    print(Utils.divider())
    print(data[['name', 'phone']])
    print('\n')

    # Afficher les deux premières
    # Colonnes uniquement
    # Troisième approche approche
    print(Utils.divider())
    print(data.loc[:, ['name', 'phone']])
    print('\n')

    # Utilisation des fonctions
    print(Utils.divider())
    data['name'] = data['name'].apply(Utils.x)
    print(data['name'])
    print('\n')

    # Utilisation des fonctions
    print(Utils.divider())
    data['name'] = data['name'] \
        .str \
        .title()
    print(data['name'])
    print('\n')

    # Faire des filtrages
    print(Utils.divider())
    print(data[data['name'] == 'Steel Joyce'])
    print(Utils.divider())
    print(data[data['name'] == 'Noelle Adams'])
    print(Utils.divider())
    print(data[data['name'] == 'Ivor Hurst'])
    print('\n')

    # Faire des modification
    # Faire un filtrage
    print(Utils.divider())
    data.loc[data['name'] == 'Steel Joyce', 'name'] = 'Alwaly AMADOU'
    data.loc[data['name'] == 'Noelle Adams', 'name'] = 'Landry BETE'
    data.loc[data['name'] == 'Ivor Hurst', 'name'] = 'Patrick Nsukami'
    print('\n')

    # Faire des filtrages
    print(Utils.divider())
    print(data[data['name'] == 'Alwaly AMADOU'])
    print(Utils.divider())
    print(data[data['name'] == 'Landry BETE'])
    print(Utils.divider())
    print(data[data['name'] == 'Patrick Nsukami'])
    print('\n')

    # Ajouter une colonne
    # Procéder par initialisation
    # Affecter une valeur arbitraire
    print(Utils.divider())
    data['age'] = 0
    data['salary'] = 0
    print(data['age'])
    print(Utils.divider())
    print(data['salary'])
    print('\n')

    # Attribuer un salaire
    # Utiliser .apply()
    # Utiliser .randin()
    print(Utils.divider())
    START = 200000
    FINAL = 1000000
    data['salary'] = data['salary'] \
        .apply(lambda x: Utils.randomize(START, FINAL))
    print(data['salary'])
    print('\n')

    # Attribuer un age
    # Utiliser .apply()
    # Utiliser .randin()
    print(Utils.divider())
    START = 18
    FINAL = 100
    data['age'] = data['age'] \
        .apply(lambda x: Utils.randomize(START, FINAL))
    print(data['age'])
    print('\n')

    # Chercher la moyenne
    # Exemple sur la colonne Salary
    # Utilisation de .mean()
    print(Utils.divider())
    print('La moyenne salariale:')
    print(data.salary.mean())
    print('\n')

    # Chercher la médiane
    # Exemple sur la colonne Salary
    # Utilisation de .median()
    print(Utils.divider())
    print('La médiane salariale:')
    print(data.salary.median())
    print('\n')

    # Chercher le maximum
    # Exemple sur la colonne Salary
    # Utilisation de .max()
    print(Utils.divider())
    print('Le salair maximal:')
    print(data.salary.max())
    print('\n')

    # Chercher le minimum
    # Exemple sur la colonne Salary
    # Utilisation de .min()
    print(Utils.divider())
    print('Le salair minimal:')
    print(data.salary.min())
    print('\n')
