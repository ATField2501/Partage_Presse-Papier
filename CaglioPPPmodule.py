""" Module du programme Partage_Presse-Papier """

import os
from cryptography.fernet import Fernet






class Hocuspocus():
    """ Class servant à encrypter et décrypter """
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    def __init__(self):    
        """ """ 
        print(Hocuspocus.key)   
    def hocus(*arg): # parmètrage implicite.. C'est la première fois que je l'utilise ^^
        """ Méthode qui encrypte une donnée"""
        message_sombre = Hocuspocus.cipher_suite.encrypt(arg[0])
        return message_sombre
    def pocus(*arg):
       """ Méthode qui décrypte une donnée """
       message_claire = Hocuspocus.cipher_suite.decrypt(arg[0])



class Nazghul(Hocuspocus): # J'adorre le principe d'héritage
    """ Class prenant en charge le coté client de l'application  """
    def __init__(self,connexion_avec_serveur):
        presse_papier= os.popen('xclip -o 2>/dev/null' ).readlines()
        presse_papier= str(presse_papier)
        b = bytes(presse_papier, 'utf-8')
        message_sombre = Hocuspocus.hocus(b)

        # On envoie le message
        connexion_avec_serveur.send(message_sombre)




class Mordor(Hocuspocus):
    """ Class prenant en charge le coté server de l'application  """
    def __init__(self):
        pass
