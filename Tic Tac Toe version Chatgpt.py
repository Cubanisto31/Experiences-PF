# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:44:55 2023

@author: paulf
"""

# Définir une fonction pour afficher le tableau
def afficher_tableau(tableau):
    print("\n")
    for i in range(3):
        for j in range(3):
            print(tableau[i][j], end=" ")
        print("\n")

# Définir une fonction pour vérifier si le joueur a gagné
def gagne(tableau, symbole):
    # Vérifier les lignes
    for i in range(3):
        if tableau[i][0] == symbole and tableau[i][1] == symbole and tableau[i][2] == symbole:
            return True
    # Vérifier les colonnes
    for j in range(3):
        if tableau[0][j] == symbole and tableau[1][j] == symbole and tableau[2][j] == symbole:
            return True
    # Vérifier les diagonales
    if tableau[0][0] == symbole and tableau[1][1] == symbole and tableau[2][2] == symbole:
        return True
    if tableau[0][2] == symbole and tableau[1][1] == symbole and tableau[2][0] == symbole:
        return True
    return False

# Définir la fonction principale pour le jeu
def jouer_tic_tac_toe():
    # Initialiser le tableau
    tableau = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    # Initialiser les symboles des joueurs
    symboles = ["X", "O"]
    # Initialiser le joueur actuel
    joueur_actuel = 0
    # Boucle principale du jeu
    while True:
        # Afficher le tableau
        afficher_tableau(tableau)
        # Demander au joueur de choisir une case
        choix = input("Joueur " + symboles[joueur_actuel] + ", choisissez une case (ex. 1,2): ")
        # Convertir la chaîne de caractères en indices de tableau
        i, j = map(int, choix.split(","))
        # Vérifier si la case est disponible
        if tableau[i-1][j-1] == "-":
            # Mettre à jour le tableau avec le symbole du joueur actuel
            tableau[i-1][j-1] = symboles[joueur_actuel]
            # Vérifier si le joueur actuel a gagné
            if gagne(tableau, symboles[joueur_actuel]):
                # Afficher le tableau
                afficher_tableau(tableau)
                # Afficher le message de victoire
                print("Joueur " + symboles[joueur_actuel] + " a gagné!")
                break
            # Vérifier si le tableau est plein (match nul)
            if all("-" not in ligne for ligne in tableau):
                # Afficher le tableau
                afficher_tableau(tableau)
                # Afficher le message de match nul
                print("Match nul!")
                break
            # Passer au joueur suivant
            joueur_actuel = (joueur_actuel + 1) % 2
        else:
            print("Case déjà occupée. Choisissez une autre case.")

# Appeler la fonction principale pour lancer le jeu
jouer_tic_tac_toe()

