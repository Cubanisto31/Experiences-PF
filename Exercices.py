# -*- coding: utf-8 -*-
"""
Created on Sun May  7 23:32:11 2023

@author: paulf
"""

 # Exercice 1 
 # Faire une concaténation de chaine de caractères  
 
 # Imaginons que l'on veuille créer une chaine de caractères qui indique "abonnne toi à ____"
 
# youtubeur = "PaulF"
 
# print(f"abonne toi à {youtubeur}") 

 # Exercice 2 
 # Faire une phrase dont certains mots font parties d'un vecteur 
 
# ville = input("Ville: ")
# adj = input("Adjectif: ")
# sport = input("Sport: ")
 
# madlib = f"Je suis content d'être à {ville}. Il y fait bon vivre et les gens \
# sont {adj}. Je peux y pratiquer le {sport} qui est mon sport préféré."

# print(madlib)

 #Exercice 3
 #Faire un programme qui choisit un nombre que je dois parvenir à deviner
# import random

# def devine(x):
#     aléatoire=random.randint(1,x)
#     devine=0
#     while devine != aléatoire :
#         devine=int(input(f'Devine un nombre entre 1 et {x}:'))
#         if devine < aléatoire:
#             print('Plus')
#         elif devine > aléatoire:
#             print('Moins')
#     print(f'Tu es chaud, tu as deviné le nombre {aléatoire}!')
        
# devine(100)

#J'aimerais rajouter un système de comptage de point en fonction du nombre de 
#tour dont il a fallu pour trouver le chiffre mystère.

 #Exercice 4
 #L'ordinateur va essayer de deviner un chiffre que j'ai dans ma tête
import random
 
def ordinateur_guess(x):
    low = 1 
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low 
        feedback = input(f'Est-ce que {guess} est supérieur (H),\
inférieur (B) ou égal(C) à ton chiffre?')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'b':
            low = guess + 1
            
    print('Bravo ordinateur, tu as trouvé')
            
    
ordinateur_guess(100)
           
            
        