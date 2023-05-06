# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:41:37 2023

@author: paulf
"""

import requests
import zipfile
import io

# URL de la page contenant les liens vers les fichiers à télécharger
url = 'https://www.data.gouv.fr/fr/datasets/5b7ffc618b4c4169d30727e0/#/resources'

# Télécharger la page HTML
response = requests.get(url)

# Extraire les liens vers les fichiers ZIP et PDF
links = []
for line in response.content.decode().split('\n'):
    if 'href=' in line and ('Télécharger la ressource' in line):
        link = line.split('href="')[1].split('"')[0]
        links.append(link)

# Télécharger les fichiers ZIP et extraire les fichiers CSV
for link in links:
    if 'Télécharger la ressource' in link:
        response = requests.get(link)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            for csv_file in zip_file.namelist():
                if csv_file.endswith('.csv'):
                    with zip_file.open(csv_file) as file:
                        # Lire le contenu du fichier CSV
                        csv_content = file.read().decode()
                        # Faire quelque chose avec les données CSV ici...

    elif 'explication' in link:
        # Télécharger les documents explicatifs PDF
        response = requests.get(link)
        with open(link.split('/')[-1], 'wb') as f:
            f.write(response.content)
