# Experiences-PF

Ce dépôt a pour objectif de répertorier les projets de PF afin de permettre de collaborer sur ces derniers ainsi que de les archiver.

Description des fichiers :

**0° .gitignore** -> Permet de ne pas commit les fichiers aux formats indiqués qui se trouveraient dans le dépôt local. 

**1° README.md** -> Permet d'indiquer l'utilité de ce dépôt ainsi que les fichiers que l'on y retrouve.

**2° Scrapping.py** -> Est un programme qui permet de télécharger les .pdf d'une page internet grâce à son URL dans un dossier pdf stocké dans le dossier à partir duquel est exécuté le programme. 

*Conseil : Exécuter le programme dans un dossier local afin d'éviter de prendre le risque de push les pdf scrappés dans le répertoire Github après un commit.*

*Amélioration possible : Il semblerait que l'URL choisit ne soit pas optimisé. Il faudrait (i) tester le programme sur une page clean et (ii) parvenir à rendre le programme plus souple afin qu'ils parviennent à réaliser des manipulations permettant de télécharger les pdf qui posent problème (ex: correction automatique des URL).*

**3° API_Insee_SIREN.py** -> Est un programme qui permet de transformer le fichier .json créé à partir d'une requête à l'API de l'insee en une base au format .csv.

*Usage : Exécuter avoir généré un fichier .json qui répertorie les objets demandés lors de notre demande à l'API de l'insee. Pour ce faire, copier/coller la sortie de l'API dans un fichier bloc-notes puis nommez le "donnees.json".* 

**4° Exercices.py** -> Est un programme qui répertorie des exercices que l'on retrouve dans la vidéo *https://www.youtube.com/watch?v=8ext9G7xspg* 

**5° TicTacToe version Google** -> Est un programme trouvé sur internet qui permet de jouer au morpion.

**6° TicTacToe version ChatGPT** -> Est un programme généré par ChatGPT qui permet de jouer au morpion. 

**7° programme projet datagouv Lucas** -> Est un code R qui créé une liste de sous bases en fonction de l'organisation qui a publié des db sur datagouv.

**8° Code sortie de poule echecs vBlaise** -> Est un code R qui permet de simuler le résultat d'une ronde suisse (règle tournoi échecs Arcep modulo l'existence des matchs nuls et la possibilité de rencontrer le même adversaire) avec n joueurs et t tours définis par l'utilisateur. 
*A terminer*

**9° Notice Excel pronostiqueur vF.docx** -> Consignes de fonctionnement du système de pronostics des résultats du tournoi de babyfoot de l'Arcep 2024 à l'intention des participants. 

**10° Excel pronostiqueur** -> Excel qui contient la formule de calcul des côtes des équipes sur la base des scores des équipes lors de la phase poule.

**11° Compilateur des resultats des pronostiqueurs.py** -> Programme qui permet de compiler les résultats transmis par les parieurs afin de calculer le nombre de points marqué par chaque parieur.

**12° Comptage jeu du rire.xlsm** -> Excel qui permet de comptabiliser les scores lors du jeu du rire. Premier usage de boutons dans excel. 

**13° Recherche doc.ipynb** -> Est un code python qui permet de rehercher tous les fichiers contenant une chaîne de caractères spécifiée dans les fichiers de l'ordinateur.

**14° Script VBA pour afficher les feuilles cachées dans un excel.txt** -> Est un script VBA qui permet, lorsqu'il est lancé dans un excel, d'afficher toutes les feuilles cachées.

**15° Fiche raccourcis.docx** -> Est une fiche qui recence des raccourcis utiles sur différents logiciels. Cette fiche a vocation a être alimentée régulièrement.
