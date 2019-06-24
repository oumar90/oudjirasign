#!/usr/bin/env python3

import time
import argparse

import codecs

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

"""
DESCRIPTION:

	Comme son nom l'indique, oudirasign est un module de signature électronique, 
	elle permet de signer numériquement les documents électronique. En plus elle permet 
	également de chiffrer/chiffre de message et bien d'autre.
	
"""

__author__="Oumar Djimé Ratou"
__copyright__="Copy Right 2019, ITS"


# Generate rsa keys
def generatersakeys(length=2048):
	""" Fonction rsakeys(bits) permet  générer une paire de clé RSA 
	elle prend en paramètre la taille de clé et reourne un tuple (privatekey, publickey).

	=============================================

	Exemple :
		(privatekey, publickey) = generatersakeys(taille) // par defaut taille=2048
	"""
	generate_random_number = Random.new().read
	key=RSA.generate(length, generate_random_number)
	privatekey = key.exportKey()
	publickey=key.publickey().exportKey()
	return privatekey, publickey

# Importation de clé privée
def importPrivateKey(privatekey):
	""" Cette fonction permet de importer la clé privé,
	 elle prend en paramètre use clé privée """
	return RSA.importKey(privatekey)

# Importation de clé public
def importPublicKey(publickey):
	""" Cette fonction permet de exporter la clé public, 
	elle prend en paramètre use clé public """
	return RSA.importKey(publickey)

# Chiffrement un message
def chiffre(message,pubkey):
	""" Cette fonction permet de chiffrer un message,
	 elle prend en paramètre le message et la clé public et retourne le message chiffré.

	 ==========================================
	
	Exemple :
		message_chiffre = chiffre(message_clair, publickey) 
	  """
	#key = RSA.importKey(open(pubkey).read()) # Si la clé est stocker sur un fichier
	cipher = PKCS1_OAEP.new(pubkey)
	ciphertext = cipher.encrypt(message.encode("utf-8"))

	return  ciphertext

# Dehiffrement d'un message
def dechiffre(ciphertext,privbkey):
	""" Cette fonction permet de déchiffrer un message, 
	elle prend en paramètre le message chiffré et la clé privée
	et retourne le message en claire.

	========================================

	Exemple :
		dechiffre = dechiffre(message_chiffre, privatekey)
	 """
	#key = RSA.importKey(open(privbkey).read()) # Si la clé est stocker sur un fichier
	cipher = PKCS1_OAEP.new(privbkey)
	message = cipher.decrypt(ciphertext).decode("utf-8")

	return message

# Fonction de hachage
def hacher(message):
	""" Cette fonction permet de hacher un message,
	 elle prend en paramètre le message en claire .
	 elle retourne le hache d'un message.

	 =======================================

	 Exemple :
	 	hache = hacher(message_clair)
	 """
	
	return SHA256.new(message.encode("utf-8"))

# Fonction de Signature
def signer(message,privatekey):
	""" Cette fonction permet de signer un message, 
	elle prend en paramètre 02 arguments, 
	le haché et la clé privée et retourne la signature.

	=========================================

	Exemple :
		signature = signer(message_claire, privatekey)
	"""
	hache = SHA256.new(message.encode("utf-8"))
	hache.hexdigest()
	sig = PKCS1_v1_5.new(privatekey)
	signature = sig.sign(hache)
	hexfy = codecs.getencoder('hex')
	ms = hexfy(signature)[0]

	# return signature
	return ms.decode("utf-8")


# Fonction de Verification
def verifier(message, publickey, signature):
	""" Cette fonction permet de verifier la signature d'un message, 
	elle prend en paramètre 03 arguments, 
	le message, la clé public et la signature. Retourne un boolean (True or False)

	=======================================

	Exemple : 
		verifier = verifier(message, publickey, signature)
	"""
	hache = SHA256.new(message.encode("utf-8"))
	# hache.hexdigest()
	signer = PKCS1_v1_5.new(publickey)

	hexfy = codecs.getdecoder('hex')
	ms = hexfy(signature)[0]

	return signer.verify(hache, ms)


def savekeys(privakeyname, publickeyname):
	""" Fonction qui permet de sauvegarder les clefs dans les fichiers 
	privatekey.txt respectivement publickey.txt"""

	with open("privatekey.pem", "w") as f_private:
		f_private.write(privakeyname)
		f_private.close()

	with open("publickey.pem", "w") as f_public:
		f_public.write(publickeyname)
		f_public.close()

def main():
	""" Fonction principale """
	# create argument parser object 
	parser = argparse.ArgumentParser(description = "Comme son nom l'indique, oudirasign est un module de signature électronique, elle permet de signer numériquement les documents et chiffrer/chiffre de message.") 
  
	parser.add_argument("-t", "--taille", type = int, nargs = 1, 
	                    metavar="taille", default = None, help = "génère une paire da clef RSA de taille t.") 


	# parse the arguments from standard input 
	args = parser.parse_args()


	print("génération de paire de clefs....")
	time.sleep(1)
	private, public = generatersakeys(args.taille[0])
	savekeys(private, public)
	print("Les clefs sont générer avec succès...")
	print("privatekey.pem, publickey.pem")
	


if __name__ == "__main__":
	main()


