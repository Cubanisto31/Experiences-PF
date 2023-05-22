# -*- coding: utf-8 -*-
"""
Created on Thu May 18 13:59:36 2023

@author: paulf
"""

# Fonction pour créer le tableau
def tableau() :
    tableau = []
    for i in range (6):
        ligne = [' ']*7
        tableau.append(ligne)
    return tableau

# Fonction pour afficher le tableau 
def afficher_tableau(tableau):
    for ligne in tableau :
        print ('|'.join(ligne))
        print ('-'*15)


# Fonction pour placer un jeton dans la colonne
# def placer_jeton() :
#     for       
