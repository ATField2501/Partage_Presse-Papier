#!/usr/bin/python3
# -*- coding: utf8 

import socket
from cryptography.fernet import Fernet
import sys
import threading
import select

#### Appelé sans argument, le serveur n'accepte que les datas cryptés
#### Si un argument lui est passé (*) , il n'accepte que les datas claires

hote = ''
port = 12800
aleph = False
actif = True
tampon1 = ''
tampon2 = ''
clients_connectes= []

if len(sys.argv) == 2:
    aleph = True

## Initialisation
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)

print("******************************************************")
print("* Presse Papier Partagé à l'écoute sur le port {} *".format(port))
print("******************************************************")

## je creer une class pour faire un thread
class Ecoute(threading.Thread):
    def __init__ (self , tampon1 , tampon2) :     
        threading.Thread.__init__(self)

    def run (self) :
        while actif:
            connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
            for connexion in connexions_demandees:
                connexion_avec_client, infos_connexion = connexion.accept()
                # On ajoute le socket connecté à la liste des clients
                clients_connectes.append(connexion_avec_client)

            client_lecture= []
        try:
            clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
        except select.error:
            pass
        else:
            # On parcourt la liste des clients à lire
            for client in clients_a_lire:
                # Client est de type socket
                msg_recu = client.recv(1024)
                msg_recu = msg_recu.decode()
                print(msg_recu)
                client.send(b"PPP-server:: OK")
                if msg_recu == "!fin":
                    serveur_lance = False



        print("Fermeture de la connexion")
        connexion_avec_client.close()



## Crypté
if aleph == False:
    key = input("Entrez la clée de décryptage: \n")
    cipher_suite = Fernet(key)

    connexion_avec_client, infos_connexion = connexion_principale.accept()

    while actif:
        msg_recu = connexion_avec_client.recv(1024)
        message_claire = cipher_suite.decrypt(msg_recu)
        print(message_claire.decode())


## Claire
else:
#    m = Ecoute(tampon1 , tampon2)  # crée le thread
#    m.start () 
     while actif:
         connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
         for connexion in connexions_demandees:
            connexion_avec_client, infos_connexion = connexion.accept()
            # On ajoute le socket connecté à la liste des clients
            clients_connectes.append(connexion_avec_client)
            olga=clients_connectes[0] 
            print(clients_connectes[0] , type(clients_connectes))


         client_lecture= []
         try:
             clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
         except select.error:
             pass

         else:
             # On parcourt la liste des clients à lire
             for client in clients_a_lire:
                 # Client est de type socket
                 msg_recu = client.recv(1024)
                 # Peut planter si le message contient des caractères spéciaux
                 msg_recu = msg_recu.decode()
                 print(msg_recu)
                 if msg_recu == "!fin":
                     serveur_lance = False


connexion_principale.close()
