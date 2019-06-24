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
	>>> privatekey, public = osy.generatersakeys() // par defaut c'est 2048 bits
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
