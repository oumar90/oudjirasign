# Module de signature électronique

oudjirasign est un module python de signature électronique.

==========================================================

[![PyPI](https://img.shields.io/badge/PyPi-v1.5-f39f37.svg)](https://pypi.org/project/oudjirasign/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/oumar90/oudjirasign/blob/master/LICENSE)

_______________________________________________________

### Prérequis

-  [Python 3.7](https://www.python.org/downloads/release/python-373/)(recommended)

-  [Pip 3](https://pip.pypa.io/en/stable/installing/)

## Installation

pour installer ce package il suffit d'ouvrir une console et tapper la commande suivante:

```
pip3 install oudjirasign
```

## Fonctionnalitées
- **génération de pair de clef RSA**
- **génération des certificats auto-signé**
- **chiffrer / déchiffrer un message**
- **signer un message grâce à la clef privée**
- **verifier la signature grâce à la clef public**

## Utilisation

- pour plus d'information, n'hésiter pas consulter l'aide, en suivant les étapes suivantes:

```python 
	>>> import oudjirasign as osy
	>>> help(osy)
```
- générer une paire de clefs

```python
	>>> import oudjirasign as osy
	>>> help(osy)
	>>> privatekey, publickey = osy.generatersakeys() # par defaut c'est 2048 bits
	>>> privatekey
	>>> b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAlNmLSdCPSH4NAkRurojzncPVoszS+KovtOD/zWkr2iMI3HdxLDVUU+bJUedM071o/+jTr89UZsuOYi64WU4RppdPeF\nseXxkDPL+3T3xhQAgnHf7JHz4IAnE49USwh+luJqEY/t5cDGPl3BvQc=\
	...\
	\n-----END RSA PRIVATE KEY-----'

	>>> public
	b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlNmLSdCPSH4NAkRurojz\nncPVoszS+KovtOD/zW\
	......\
	\n-----END PUBLIC KEY-----'
	>>> 
```
- chiffrer / déchiffrer un message

```python
	>>> message = "Hello world"
	>>> chiffre = osy.chiffre(message, publickey)
	>>> privatekey= osy.importPrivateKey(privatekey)
	>>> public= osy.importportPublicKey(public)
	>>> chiffre = osy.chiffre(message, public)
	>>> chiffre
	b'?\xcfPlz\xd9\xac\x89\x91~\xf3\xd5-@\x86\xac\xdf\xb5/\xffH\xdd\xf3&\xa7@iX}+\xe4\x08\xe6\x83\xadQ\x95\xb3\x07\xe9\xa3\xd1\x8d\xff\xb5\xd2\t\x88\xda\xddI\xdd\xdfq\xe0\x9f\xc0\x9e\x96\xca\x83\x18T\xfb\x81\n\xe6X\xb5}y\xe0Q\x02\xb6g\xae\x08\xa7\x17\xba\xbe6\xbc\x08\x16(%\xaa^t5s\xd9\xce5d$\xa5\x95\xfd\xcf42\x1d\x00\x9f/ai\x15\xafze\xc6kK\xa75\x9d\xa6xJ=\xd6\x95\xe2\xed\x8a\xc3\xc32\xd3\xce\xf4F`f3H\x0f+\\\xe5z`\xce\x15Q\xb3\xe2\xbf\xfe_\xbc\xf3\x8a\x91\xe8\x93\x04_\t2\x902[\xc1\x9d\xca\xe8\xae\xfbD\x89\x87\xda\xd6\x1f\n&\n\x93\x84k\xfc\x14\xed\x836N\xd0\xfd9\xf9\xa1\xbds\x9d(\xca*\x9a7\xf9\xdc\xed\xd7\x8b\xb8\x03yL\x8f\xc2\xeaz\xb2\xcdw1\xbd\x95#\xd6}\xaf\xd4{\xcdc\xfd\x1ah\xa2\xdb\x9a\xdc"\x03\x92i\xe0\xa9>\xbb\xe1\xb9p\x7f \xa4Lt\x8bs'
	>>> 
	>>> dechiffre = osy.dechiffre(chiffre, privatekey)
	>>> 
	>>> dechiffre
	'Hello world'
```
- signer / verifier un message
```python
	>>> signature = osy.signer(message, privatekey)
	>>> 
	>>> signature
	'a1e7660f532b0374bf476f35f3b2e6bc0eb07dfa771f816aaccac08c184c972a96dafccd0851df88b6398b37773a2d3ba03028187dd5e6c92a42ca0762c07ff1d157de5daf486b31b3c6f1da506fe5a3c0a2be2260e0e47175b37f9896994b3f340603c09d48502f4aff4e3895d57b5e751c8592e0ed33fdb9e4a3610bbb58402ff235237acd874db1dc8b6f318328415fcae9687812b1caa8d65bfb74da49ffdc36c0f0946165fb1f97f74d6de43f3d5e982674de7b24c52bfd88653885b692331e5523e8676a5d90ef81302a38c33ca4391d035545d19cdd1479b2a4ea015877ab39780221be425a28f6439b40f4d51e91414294ca5792eb2108abc228c8f5'
	>>> 
	>>> 
	>>> verifier = osy.verifier(message, public, signature)
	>>> 
	>>> verifier
	True
```
- Pour générer un certificat auto-signé, il suffit tapper la commande suivante dans le console :
```bash
	$ oudjirasign -t 2048
	génération de paire de clefs... |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@| 100% # Bar de progression

	Les clefs sont générées avec succès et sont stockées dans les fichiers ci-dessous.
	privatekey.pem, publickey.pem

	Voulez-vous générer un certificat associé à votre votre paire de clef(Y/n\) : y
	génération du certificat en cours...
	Entrer le nom de votre pays : [Ex. CM, pour Cameroun] : cm
	Entrer le nom de l\'État ou de la province : [Ex. Centre] : centre
	Entrer le nom de votre ville : [Ex. Yaoundé] : yde
	Entrer le nom de votre organisation : [Ex. ITS] : its
	Entrer le nom de votre section : [Ex. SECURITÉ] : info
	Entrer le nom de domaine : [Ex. groupits.cm] : groupits.cm
	Le certificat est généré avec succès.
	$
```
