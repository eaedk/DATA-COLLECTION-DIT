# Rest API
# URLs, Domain, Names and IP Address


# Une URL est composée des parties:
#   Le PROTOCOLE (http/https/sftp/ftp)
#   Le domain (DNS)
#   Les paramètres de l'URL
#   La syntaxe {protocole}://{domain}/{params}
#   Exemple:
#     - https://dit.sn/
#     - https://www.youtube.com/watch?v=DYFD1p7BGZc
#       - {protocole}: https
#       - {domain}: youtube.com/www.youtube.com
#       - {path}: watch
#       - {v}: query parameter
#       - {DYFD1p7BGZc}: Filtering Value of {v}


# Une Adresse IP est composé de:
#   Quatre Octets (IPV4)
#   Six Octets (IPV6)
#   Chaque Octet est de 8 bits codé de 0-255
#   Exemple:
#     - 154.168.10.98
#     - 127.0.0.1
#     - 192.168.0.1
#   La résolution d'une Adresse IP est le process de DNS
#   A un domain on associe une Adresse IP
#   On peut avoir des sous domaines.
#   La résolution se fait de la même manière
#   On a aussi le processus de résolution inverse


# Une API est une interface permettant de dialoguer pour extraire des données
# Les données sont transmises via une requette HTTP/HTTPS
# Les données sont soumis a différentes normes de formattage
#   - du REST (plus flexible) (format de donnée: JSON)
#   - du SOAP (plus sécurisé / Mais rigide) (format de donnée: XML)
# Les actions possibles sont:
#   - GET (safe Method) (utilisation des paramètres URLs)
#   - POST
#   - PUT
#   - PATCH
#   - DELETE
#   - OPTION
#   - HEAD (safe Method)
# Pour traduire l'état de la requete HTTP on a des status
# Ces status décrivent l'état de la réponse ou de la requête
#   - 200 (OK)
#   - 201 (CREATED)
#   - 302 (REDIRECTION)
#   - 400 (BAD REQUEST)
#   - 401 (UNAUTHORIZED)
#   - 500 (SERVER ERROR)
#   - 503 (SERVICE UNAVAILABLE)
#   - 504 (GATEWAY TIMEOUT)
# Donc en conclusion pour utiliser une API
#   - requête (GET/POST/...) + URL --> Status (200/...)
#   - Il faudra utiliser un client HTTP
