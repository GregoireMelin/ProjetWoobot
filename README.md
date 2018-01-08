# PROJET WOOBOT
# Composition du depot :
	- configure.sh (permet d'installer les dépendances via la commande : sudo bash configure.sh
	- script_ur.py (script courant)
	- README.txt (indications)


# PARAMETRES DE CONNEXION (Ethernet/IP) --> Brancher le robot avec un câble ethernet sur l’ordinateur
## SUR LE ROBOT :
- Démarrer le robot
- Allez dans l’onglet « Configuration du robot »
- Allez dans l’onglet « Réseau »
- Sélectionner l’option : Adresse statique
- Dans la partie « Réglages détaillés du réseau » 
	Adresse IP : 192.168.1.196
	Masque sous-réseau : 255.0.0.0
	Passerelle par défaut : 0.0.0.0
	Serveur DNS préféré : 0.0.0.0
	Serveur DNS alternatif : 0.0.0.0

- Sélectionner « Appliquer », attendre une minute, le robot devrait se connecter et devrait afficher « Le réseau est connecté ».

## SUR LE PC --> Allez dans les paramètres réseau & créer une nouvelle connexion filaire


- Onglet "Filaire"
- Cliquer sur « Nouveau profil »

- Allez dans l’onglet IPv4
- Renseignez les champs suivants dans les champs "adresse":
	Sur la ligne adresse sélectionner : "Manuel"
	-----------------------
	Adresse : 192.168.0.196
	Masque sous-réseau : 255.0.0.0
	Passerelle  : 0.0.0.0

## DANS LE SCRIPT :
Renseignez la ligne de construction :
rob = urx.Robot("192.168.1.196")
	

# RESSOURCES :
- Depot Git de python-urx : https://github.com/SintefRaufossManufacturing/python-urx
- Site support : https://www.universal-robots.com/how-tos-and-faqs/how-to/


