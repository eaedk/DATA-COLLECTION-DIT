## Exercice 1

___

* Ecrire une fonction du nom de <code>readJson(filepath: str)</code> qui permet de récupérer les données du fichier <code>file.json</code>

* Ecrire une fonction qui permet de déserailaiser la donnée en la transformant en Dictionnaire tout en utilisant la bibliothèque json de python

```python3
import json

```

* Ecrire une fonction qui permet de récupérer le noeud list du nouveau dictionnaire obtenu afin d'en faire une vraie liste python en prenant en compte la caractère de séparation <code>","</code>

* Appliquer la fonction de la question précédente pour obtenir une liste python comme valeur pour la clé list du dictionnaire obtenue. Ainsi à la fin de ce traitement vous devez obtenir un nouveau dictionnaire contenant en plus des autres clés la clé list qui sera de type <code> list</code>

* A l'aide des utilitaires <code>filter</code> et <code>map</code> et des utilitaires utilies au traitement des données et de la restructuration des données, il faudra reconstruire le dictionnaire en suivant les régles suivantes:
    * mettre le nom + prénom obtenu de la séparation de la valeur de la clé <code>name</code> sous une nouvelle clé du nom <code>informations_personnelles</code>
    * remettre les informations bancaires se trouvant dans le dictionnaire obtenu sous une nouvelle clé du nom <code>informations_bancaires</code>
