# Les Listes compréhension
# Les LISTES/DICT
# COLLECTION DE DONNEES
#
# Les sources de données
# Les fichiers
# 	- TXT (Fichiers texts)
# 		- Utilisation des fonction I/O
# 			- Utilisation de open()
# 	- CSV (Extension .csv) (,/)
# 		- Utilisation des fonction I/O
# 			- Utilisation de open()
# 			- Utilisation de PANDAS (Module)
# 			- Utlisation de NUMPY (Module)
# 			- Utlisation de CSV (Module)
# 	- EXCEL (Extension .xlx/.xlxs)
# 	 	- Utilisation de open()
# 	 	 	- Utilisation de PANDAS (Module)
# 	 	 	- Utlisation de NUMPY (Module)
#    		- Utlisation de CSV (Module)
# 	- JSON (Format KEY/VALEUR)
# 		- Il ressemble au DICTIONNAIRE en python
# 		- JSON(STR) et DICT (DICT)
# 	- DATABSE(SQL/PL/SQL)
# 		- Langage natif SQL
# 		- Langage de requêtes
# 			- CREATE STATEMENT
# 			- SELECT STATEMENT (*)
# 			- UPDATE STATEMENT
# 			- JOIN STATEMENT
# 			- WHERE STATEMENT (*)
# 			- GROUP BY STATEMENT (*)
# 			- ORDER BY STATEMENT
# 			- BETWEEN STATEMENT
# 			- LIKE/NOT LIKE STATEMENT
# 			- Operations COUNT/SUM/AVG...
# 			- AGGREGATION (Sql Avancé)
# 			- PIVOT STATEMENT (Sql Avancé)
# 	- APIs RESTFUL (Json data) / API SOAP (XML)
# 		- Une API a une documentation
# 			- De savoir comment formuler la requêtes
# 			- Quels sont les éléments important à mettre dans:
# 				- LE BODY
# 				- LE HEADER
# 				- L'URL
# 				- Les PARAMS
# 			- Exemple de DOC API
# 				- URL: (https://restcountries.com/#api-endpoints-v2-all)
# 				- ENDPOINT === URL
# 		- Le serveur qui répond a des demandes
# 		- Les demandes des clients
# 			- Sont ceux qui transcrive la requête
# 			- YOUTUBE (Serveur GOOGLE (Adresse IP qui font la même résolution inversée))
# 			- YOUTUBE (XXXX.XXXX.XXXX.XXXX)
# 			- L'application de youtube (WEB/MOBILE)
# 				- sont des clients
# 				- Ils enverrons une requête HTTP/HTTPS
# 				- HTTP est un protocole
# 				- HTTPS (HTTP+SSL)
# 				- SSL aussi est un protocole de sécurité
# 					- Certificat
# 					- La clé privée
# 					- La clé publique
# 			- Un module du nom de REQUESTS
# 				- Qui permet de formuler des requêtes HTTP
# 				- Ces verbes traduisent l'action a faire par le serveur
# 					- GET (Lire une ressource)
# 					- POST (Créer une resource)
# 					- PUT (Mettre à jour une ressource)
# 					- PATCH (Mettre à jour une ressource partielle)
# 					- DELETE (Supprimer une ressource)
# 					- OPTION (....)
# 					- HEAD (....)
# 				- CRUD (GET/POST/PUT/PATCH/DELETE)
# 					- CREATE ==> (POST: 201)
# 					- READ ==> (GET/HEAD: 200)
# 					- UPDATE ==> (PUT/PATCH: 200/2XX)
# 					- DELETE ==> (DELETE: 204)
# 			- Communication dans 2 sens
# 				- Serveur <==> Client
# 				- Client <==> Serveur
# 					- Via requêtes HTTP
# 					- Les Status codes
# 						- qui défnissent l'état de la requête
# 						- 2XX
# 							- 200: OK (GET/POST/PUT/PATCH)
# 							- 201: CREATED (POST)
# 							- 204: NO CONTENT (DELETE)
# 						- 3XX
# 						- 4XX
# 							- 404: NOT FOUND (*)
# 							- 401: UNAUTHORIZED (*)
# 							- 400: BAD REQUEST (*)
# 						- 5XX
# 							- Souvent lié au serveur
# 		- Utilisation du module JSON
# 		- Utilisation du module REQUESTS
# 			- URL DOC (https://requests.readthedocs.io/en/latest/)
# 		- Scénario
# 			- URL (https://restcountries.com/4144141441)
# 			- RESPONSE ("message": "Page Not Found")
# 				- PAYLOAD:
# 					- message est la clé
# 					- Page Not Found est la valeur
# 		- Les clients HTTP
# 			- Qui permettent de teste/faire une requêtes HTTP
# 			- C'est l'outils POSTMAN/INSOMNIA
# 			- VSCODE intégre des clients de requêtes HTTP
# 			- Quand on parle de COLLECTION
# 				- Ce sont des resources
# 				- Requêtes...
# 			- Pour télécharger POSTMAN
# 				- URL (https://www.postman.com/downloads/)
# 		- Les réponses de type TEXT (contenu HTML) sont aussi des formats de réponses
# 			- Le format dépend du format choisi dans le HEADER
# 				- On peut donc définir:
# 					- Un format HTML
# 					- format JSON
# 					-...
# 				- Pour définir cet format dan le HEADER
# 					- On utilise Content-Type: application/json
# 		- Une requêtes
# 			- CORPS (BODY)
# 			- TETE (HEADERS)
# 			- URL
# 			- PARAMS
# 		- Exemple d'appel API (PART 1)
# 			- URL (https://restcountries.com/v3.1/all)
# 			- PROCOLE DE SECURITE (SSL)
# 			- ACTION (GET)
# 			- HEADER (Content-Type: application/json)
# 			- PARAMS (  )
# 			- PAYLOAD:
# 				- format JSON
# 				- statutCode est de 200
# 		- Exemple d'appel API (PART 2)
# 			- URL (https://restcountries.com/v3.1/name/{name})
# 			- PROCOLE DE SECURITE (SSL)
# 			- ACTION (GET)
# 			- HEADER (Content-Type: application/json)
# 			- PARAMS ({name})
# 				- Exemple: Afghanistan
# 			- PAYLOAD:
# 				- format JSON
# 				- statutCode est de 200
# 		- Les statutCode de succès
# 			- 200
# 			- 201
# 			- 301/302 (Redirtection)
#   - SITES HTML (Extensions .html/.htm)
#   	- Utilisation du WEB SCRAPING
#   		- Mette en place des systèmes pour cacher la données
#   		- Les sites payants ou les sites professionnels
#   			- C'est un site (HTML/CSS/JS)
#   			- Fichiers statiques (HTML/CSS/JS/IMAGES/ICONS)
#   				- Tout ce qui est accessible au grand public
#   				- JS...(50/50)
#   				- Exemple:
#   					- URL (https://www.imdb.com/)
#   					- URL (view-source:https://www.imdb.com/)
#   			- Dont le contenu (CSS/JS) ont été comiplé
#   				- Compiler des outils de compilations...
#   				- Lire la données avec du WEB SCRAPING er compliqué
#   	- Utlisation du module BeautifulSoup (BS4)
#
# Les différentes types de bases de données
# 	- MYSQL (Langage de base SQL)
# 	- ORACLE (Langage de base PL/SQL)
# 	- POSTGRESQL (Langage de base SQL)
# Trouver le moyen de collecter ces données
# Avec du python (STRUCTURE DE DONNEE)
# Avec du python (SHALLOW and DEEPCOPY)
#
#
# Cacher les données importantes
# Utilisation d'une API avec le fichier .env
# Headers:
# 	- Des données d'authentification
# 	- On a les données (KEY API/TOKEN/Etc...)
# 		- TOKEN (Headers D'authorisation)
# 		- KEY API aussi (Authentification/Authorisation)
# 		- Ce sont des données à protéger
# 		- Pour faire cette Protection:
# 			- Module python-dotenv
# 			- Qui utilise un fichier d'environnement
# 			- URL de python-dotenv (https://pypi.org/project/python-dotenv/)
# 			- Pour l'utilisation:
# 				- Créer un fichier .env a la racine du projet
# 				- Exemple d'API avec une API KEY
# 					- URL (https://apilayer.com/marketplace/currency_data-api)
# 					- Pour afficher les variables d'environnements
# 						- import os
# 						- from dotenv import load_dotenv
# 						- load_dotenv()
# 						- os.environ.get('API_KEY')
# 						- le nom API_KEY n'est pas figé
# 						- il dépendra de votre nommenclature
#
# Le SCRAPPING
# - Pour les formats de données nous avons
# 	- XML
# 	- JSON
# 	- TEXT/PLAIN
# 	- HTML
#
# Le Scrapping match avec le format HTML
# - Ainsi le format HTML est le format des fichiers .html/.htm
# - Pour cela le module requests est utilisé
# - Faire la requête en GET
# - Récupérer le contenu en STRING
# - Puis le PARSER avec du BeautifulSoup
# - Installer donc le module BS4 de python
# - Les outils indispensables sont donc:
# 	- module requests
# 	- module bs4
# 		- URL (https://pypi.org/project/beautifulsoup4/)
# 		- DOC (https://beautiful-soup-4.readthedocs.io/en/latest/)
# 	- URL de site WEB(.html/.html)
# 	- Exemple de site WEB:
# 		- URL (https://dit.sn/)
# 		- SCRAPPING de DIT...
# 		- Procédure de scrapping
# 			- Afficher le code source de la page
# 			- Faire une requete GET sur l'URL
# 			- Parser avec BeautifulSoup
# 			- Obtenir ainsi l'instance de BeautifoulSoup
# 				- Trouver des éléments du DOM avec les TAGS
# 					- <meta property="og:locale" content="fr_FR" />
# 					- meta est un TAG (Balise)
# 				- Pour récupérer la liste on utilise
# 					- la fonction find_all()
# 					- la fonction find_all(<TAG>)
#
