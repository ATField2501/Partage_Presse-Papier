#!/usr/bin/python3
# -*- coding: utf8 

import socket
from cryptography.fernet import Fernet
import sys

#### Appelé sans argument, le serveur n'accepte que les datas cryptés
#### Si un argument lui est passé (*) , il n'accepte que les datas claires

hote = ''
port = 12800
aleph = False

if len(sys.argv) == 2:
    aleph = True

## Initialisation
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)


print("Presse Papier Partagé à l'écoute sur le port {}".format(port))



## Crypté
if aleph == False:
    key = input("Entrez la clée de décryptage: \n")
    cipher_suite = Fernet(key)

    connexion_avec_client, infos_connexion = connexion_principale.accept()

    while 1:
        msg_recu = connexion_avec_client.recv(1024)
        message_claire = cipher_suite.decrypt(msg_recu)
        print(message_claire.decode())
    print("Fermeture de la connexion")
    connexion_avec_client.close()
    #connexion_principale.close()


## Claire
else:
    connexion_avec_client, infos_connexion = connexion_principale.accept()

    while 1:
        msg_recu = connexion_avec_client.recv(1024)
        message_claire = cipher_suite.decrypt(msg_recu)
        print(message_claire.decode())
    print("Fermeture de la connexion")
    connexion_avec_client.close()
