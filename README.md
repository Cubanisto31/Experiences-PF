# Experiences-PF

Ce dépôt a pour objectif de répertorier les projets de PF afin de permettre de collaborer sur ces derniers ainsi que de les archiver.

Description des fichiers :

**1° README.md** -> Permet d'indiquer l'utilité de ce dépôt ainsi que les fichiers que l'on y retrouve.

**2° Scrapping.py** -> Permet de télécharger les .pdf d'une page internet grâce à son URL dans un dossier pdf stocké dans le dossier à partir duquel est exécuté le programme. 
*Conseil : Exécuter le programme dans un dossier local afin d'éviter de prendre le risque de push les pdf scrappés dans le répertoire Github après un commit.*

*Amélioration possible : Il semblerait que l'URL choisit ne soit pas optimisé. Il faudrait (i) tester le programme sur une page clean et (ii) parvenir à rendre le programme plus souple afin qu'ils parviennent à réaliser des manipulations permettant de télécharger les pdf qui posent problème (ex: correction automatique des URL)*

**3° API_Insee_SIREN** -> Permet de transformer le fichier .json créé à partir d'une requête à l'API de l'insee en une base au format .csv.
*Usage : Exécuter avoir généré un fichier .json qui répertorie les objets demandés lors de notre demande à l'API de l'insee. Pour ce faire, copier/coller la sortie de l'API dans un fichier bloc-notes puis nommez le donnees.json* 




