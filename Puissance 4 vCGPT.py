# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:10:52 2023

@author: paulf
"""

# Fonction pour créer un tableau vide
def creer_tableau():
    tableau = []
    for _ in range(6):
        ligne = [' '] * 7
        tableau.append(ligne)
    return tableau

# Fonction pour afficher le tableau
def afficher_tableau(tableau):
    for ligne in tableau:
        print('|'.join(ligne))
        print('-' * 15)

# Fonction pour placer un jeton dans une colonne
def placer_jeton(tableau, colonne, jeton):
    for i in range(5, -1, -1):
        if tableau[i][colonne] == ' ':
            tableau[i][colonne] = jeton
            return True
    return False

# Fonction pour vérifier si un joueur a gagné
def gagne(tableau, symbole):
    # Vérifier les lignes
    for ligne in tableau:
        for colonne in range(4):
            if ligne[colonne] == symbole and ligne[colonne + 1] == symbole and \
               ligne[colonne + 2] == symbole and ligne[colonne + 3] == symbole:
                return True

    # Vérifier les colonnes
    for colonne in range(7):
        for ligne in range(3):
            if tableau[ligne][colonne] == symbole and tableau[ligne + 1][colonne] == symbole and \
               tableau[ligne + 2][colonne] == symbole and tableau[ligne + 3][colonne] == symbole:
                return True

    # Vérifier les diagonales ascendantes
    for colonne in range(4):
        for ligne in range(3, 6):
            if tableau[ligne][colonne] == symbole and tableau[ligne - 1][colonne + 1] == symbole and \
               tableau[ligne - 2][colonne + 2] == symbole and tableau[ligne - 3][colonne + 3] == symbole:
                return True

    # Vérifier les diagonales descendantes
    for colonne in range(4):
        for ligne in range(3):
            if tableau[ligne][colonne] == symbole and tableau[ligne + 1][colonne + 1] == symbole and \
               tableau[ligne + 2][colonne + 2] == symbole and tableau[ligne + 3][colonne + 3] == symbole:
                return True

    return False

# Fonction principale pour exécuter le jeu
def jouer_puissance4():
    tableau = creer_tableau()
    joueur = 'X'
    fin_jeu = False

    while not fin_jeu:
        afficher_tableau(tableau)
        colonne = int(input("Joueur {} : Choisissez une colonne (0-6): ".format(joueur)))

        if colonne < 0 or colonne > 6:
            print("Choix invalide. Veuillez choisir une colonne entre 0 et 6.")
            continue

        if not placer_jeton(tableau, colonne, joueur):
            print("Colonne pleine. Veuillez choisir une autre colonne.")
            continue

        if gagne(tableau, joueur):
            afficher_tableau(tableau)
            print("Le joueur {} a gagné !".format(joueur))
            fin_jeu = True
            break

        if tableau_plein(tableau):
            afficher_tableau(tableau)
            print("Match nul !")
            fin_jeu = True
            break

        # Changer de joueur
        joueur = 'O' if joueur == 'X' else 'X'

    choix = input("Voulez-vous jouer à nouveau ? (O/N): ")
    if choix.upper() == 'O':
        jouer_puissance4()
    else:
        print("Merci d'avoir joué !")

# Fonction pour vérifier si le tableau est plein
def tableau_plein(tableau):
    for ligne in tableau:
        if ' ' in ligne:
            return False
    return True

# Appel de la fonction principale pour démarrer le jeu
jouer_puissance4()
