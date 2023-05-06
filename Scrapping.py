# -*- coding: utf-8 -*-
"""
Created on Sat May  6 01:35:25 2023

@author: paulf
"""

import os 
import requests
from bs4 import BeautifulSoup

# Spécifiez l'URL de la page web contenant les fichiers PDF à télécharger
url = 'https://www.arcep.fr/la-regulation/grands-dossiers-thematiques-transverses/la-diffusion-audiovisuelle-hertzienne-terrestre-ex-marche-18.html'

# Envoyez une requête HTTP GET pour obtenir le contenu de la page web
response = requests.get(url)

# Analyser le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Créez un dossier pour stocker les fichiers PDF téléchargés
if not os.path.exists('pdf'):
    os.makedirs('pdf')
    
# Trouvez tous les liens vers les fichiers PDF sur la page
pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]   

# Téléchargez chaque fichier PDF dans le dossier "pdf"
for link in pdf_links:
    # Vérifier et corriger l'URL si nécessaire
    if not link.startswith('http://') and not link.startswith('https://'):
        link = 'http://' + link
    
    file_name = link.split('/')[-1]
    file_path = os.path.join('pdf', file_name)
    try:
        response = requests.get(link)
        response.raise_for_status()  # Vérifier si une erreur s'est produite
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f'Téléchargement de {file_name} terminé')
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération du fichier PDF à partir de l'URL {link}: {e}")
