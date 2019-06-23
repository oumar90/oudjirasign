#!/usr/bin/env python3


import codecs

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

"""
Comme son nom l'indique, oudirasign est un module de signature électronique, 
elle permet de signer numériquement les documents et chiffrer/chiffre de message.
"""

__author__="Oumar Djimé Ratou"
__copyright__="Copy Right 2019, ITS"


# Generate rsa keys
def generatersakeys(taille=2048):
	""" Fonction rsakeys(bits) permet  générer une paire de clé RSA 
	elle prend en paramètre la taille de clé, exemple : 2048.*
	"""
	generate_random_number = Random.new().read
	key=RSA.generate(taille, generate_random_number)
	privatekey = key.exportKey()
	publickey=key.publickey().exportKey()
	return privatekey.decode('utf-8'), publickey.decode('utf-8')

# Exportation de clé privée
def importPrivateKey(privatekey):
	""" Cette fonction permet de importer la clé privé, elle prend en paramètre use clé privée """
	return RSA.importKey(privatekey)

# importation de clé public
def importPublicKey(publickey):
	""" Cette fonction permet de importer la clé public, elle prend en paramètre use clé public """
	return RSA.importKey(publickey)

# Chiffrement un message
def chiffre(message,pubkey):
	""" Cette fonction permet de chiffrer un message, elle prend en paramètre le message et la clé public """
	#key = RSA.importKey(open(pubkey).read()) # Si la clé est stocker sur un fichier
	cipher = PKCS1_OAEP.new(pubkey)
	ciphertext = cipher.encrypt(message.encode("utf-8"))

	return  ciphertext

# Dehiffrement d'un message
def dechiffre(ciphertext,privbkey):
	""" Cette fonction permet de déchiffrer un message, 
	elle prend en paramètre le message chiffré et la clé privée """
	#key = RSA.importKey(open(privbkey).read()) # Si la clé est stocker sur un fichier
	cipher = PKCS1_OAEP.new(privbkey)
	message = cipher.decrypt(ciphertext).decode("utf-8")

	return message

# Fonction de hachage
def hacher(message):
	""" Cette fonction permet de hacher un message, 
	elle prend en paramètre le message en claire """
	
	return SHA256.new(message.encode("utf-8"))

# Fonction de Signature
def signer(message,pvkey):
	""" Cette fonction permet de signer un message, 
	elle prend en paramètre 02 arguments, 
	le haché et la clé privée 
	"""
	hache = SHA256.new(message)
	sig = PKCS1_v1_5.new(privatekey)
	signature = sig.sign(hache)
	hexfy = codecs.getencoder('hex')
	ms = hexfy(signature)[0]

	return ms.decode("utf-8")

# Fonction de Verification
def verifier(message, pbkey, signature):
	""" Cette fonction permet de verifier la signature d'un message,
	 elle prend en paramètre 03 arguments, 
	le haché, la clé public et la signature 
	"""
	hache = SHA256.new(message)
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

