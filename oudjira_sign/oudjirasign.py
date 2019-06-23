import time
import argparse
from module import *


def main():
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