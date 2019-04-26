#!/usr/bin/python3
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com
# Utilitaire qui enregistre le presse papier pour le transmettre à une machine sous android

import os
import socket
import time
import sys


from config import *
from CaglioPPPmodule import *

aleph = False

# si argument passer à la commande on enclenche le mode crypté
# Lecture des arguments
if len(sys.argv) == 2:
    aleph = True



#Création du client
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Création du serveur
#connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connexion_principale.bind((hote, port))
#connexion_principale.listen(5)
#connexion_avec_client, infos_connexion = connexion_principale.accept()       


#Connexion avec le serveur
try:
    connexion_avec_serveur.connect(server)
except Exception as e:
    print(str(e))


## Claire
if aleph == True:
    while 1:
        presse_papier= os.popen('xclip -o 2>/dev/null' ).readlines()
        presse_papier2=""
        for e in presse_papier:
            presse_papier2 += e
        if len(presse_papier2) != 0:
            b = bytes(presse_papier2, 'utf-8')
            # On envoie le message
            connexion_avec_serveur.send(b)
        time.sleep(0.6) 

    connexion_avec_serveur.close()

## Crypté
else:
    #On génère un clée de cryptage
    crypt=Hocuspocus()
    while 1:
        obj=Nazghul(connexion_avec_serveur)
        msg_recu = connexion_avec_serveur.recv(1024)
#    msg_recu = connexion_avec_client.recv(1024)
        time.sleep(0.6) 
    connexion_avec_serveur.close()


