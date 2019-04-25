#!/usr/bin/python3
# -*- coding: utf8 

import socket
from cryptography.fernet import Fernet

hote = ''

port = 12800


connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)



print("Le serveur écoute à présent sur le port {}".format(port))


key = input("Entrez la clée de décryptage: \n")
cipher_suite = Fernet(key)

connexion_avec_client, infos_connexion = connexion_principale.accept()



while 1:
    msg_recu = connexion_avec_client.recv(1024)
    message_claire = cipher_suite.decrypt(msg_recu)
    print(message_claire.decode())
    connexion_avec_client.send(b"5 / 5")
print("Fermeture de la connexion")

connexion_avec_client.close()
connexion_principale.close()
