#PROJET API Lucas#

#Code permettant de nettoyer la base de données télécharger à l'adresse ci-dessous
#https://doc.data.gouv.fr/api/telecharger-un-catalogue-de-donnees/
#"Télécharger le catalogue des jeux de données"

#Un travail de désencodage manuel a été réalisé en amont, pas clean 

library(readr)
library(tidyverse)
#Importer la base de données désencodée 
df <- read_delim("Tableau de donnees.csv", 
                                 delim = ";", escape_double = FALSE, trim_ws = TRUE)

#Ne garder que les variables intéressantes
df_clean <- subset(df, select = c("id","title","url","organization","organization_id","quality_score"))

#Compter le nombre de bases par différentes organisations 
org_group <- df_clean %>% group_split(organization)


# Trier les sous-listes en fonction du nombre de lignes


