# Module de signature numérique

oudjirasign est un module python de signature électronique.

### Prérequis

-  [Python 3.7](https://www.python.org/downloads/release/python-373/)  (recommended)

```
pip3 install pycrypto
 ```

## Installation

pour installer ce package il suffit d'ouvrir une terminal et tapper la commande suivante:

```
pip3 install oudjirasign
```

## Fonctionnalités
- **génération de pair de clef RSA**
- **chiffrer / déchiffrer un message**
- **signer un message grâce à la clef privée**
- **verifier la signature grâce à la clef public**

## Utilisation

- générer une paire de clefs
```
	>>> import oudjirasign as osy
	>>> help(osy)
	>>> privatekey, publickey = osy.generatersakeys() // par defaut c'est 2048 bits
	>>> privatekey
	>>> b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAlNmLSdCPSH4NAkRurojzncPVoszS+KovtOD/zWkr2iMI3HdxLDVUU+bJUedM071o/+jTr89UZsuOYi64WU4RppdPeF\nseXxkDPL+3T3xhQAgnHf7JHz4IAnE49USwh+luJqEY/t5cDGPl3BvQc=
	...
	\n-----END RSA PRIVATE KEY-----'

	>>> public
	b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlNmLSdCPSH4NAkRurojz\nncPVoszS+KovtOD/zW
	......
	\n-----END PUBLIC KEY-----'
	>>> 
```
- chiffrer / déchiffrer un message

```
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