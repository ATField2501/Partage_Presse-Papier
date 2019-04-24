#!/usr/bin/python3
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com
# Utilitaire qui enregistre le presse papier pour le transmettre à une machine sous android

import os
import socket
import time
from config import *

#Création du client
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connexion avec le serveur
try:
    connexion_avec_serveur.connect(server)
except Exception as e:
    print(str(e))

class Nazghul():
    def __init__(self):
        # On fait appel à la commande système xclip, on verifie son etat et si == 0  on sauvegarde le presse papier dans une variable qu'on envois au serveur après l'avoir encoder en une chaine de bytes.
#        if os.system('xclip -o 2>/dev/null' ) == 0:
        presse_papier= os.popen('xclip -o 2>/dev/null' ).readlines()
        presse_papier= str(presse_papier)
        self.msg_a_envoyer = presse_papier.encode()

           
while 1:
    obj=Nazghul()
    # On envoie le message
    connexion_avec_serveur.send(obj.msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    time.sleep(0.6) 

connexion_avec_serveur.close()
