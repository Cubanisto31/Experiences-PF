# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:41:37 2023

@author: paulf
"""


import pandas as pd 
import json 

# Charger les données JSON à partir d'une chaîne ou d'un fichier
with open('donnees.json', 'r') as f:
    donnees_json = json.load(f)

# Extraire les informations nécessaires et les stocker dans une liste de dictionnaires
unites_legales = donnees_json['unitesLegales']
liste_informations = []
for unite_legale in unites_legales:
    siren = unite_legale['siren']
    date_creation = unite_legale['dateCreationUniteLegale']
    categorie = unite_legale['categorieEntreprise']
    denomination = unite_legale['periodesUniteLegale'][0]['denominationUniteLegale']
    activite_principale = unite_legale['periodesUniteLegale'][0]['activitePrincipaleUniteLegale']
    informations = {'SIREN': siren, 'Date de création': date_creation, 'Catégorie': categorie, 'Dénomination': denomination, 'Activité principale': activite_principale}
    liste_informations.append(informations)

# Créer un DataFrame à partir de la liste de dictionnaires
df = pd.DataFrame(liste_informations)

# Exporter le DataFrame au format CSV
df.to_csv('donnees.csv', index=False)