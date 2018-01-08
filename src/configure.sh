#!/bin/bash


# INSTALLATION DEPENDANCES
#installer Pip
echo " -- Installation de l'outil pip  -- "
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
#installation de la bilbiotheque UR-X
echo " -- Installation de la bibliotheque urx  --"
sudo pip install urx
#Installation de la bibliothèque transforms3d
echo " -- Installation de la bibliotheque transforms3d --"
sudo pip install transforms3d


