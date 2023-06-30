#Simulation d'un grand nombre de sortie de poule selon les règles du tournoi
#d'échecs de l'Arcep en 2023


#Définir n 
n <- 128

# Pour la reproductibilité des résultats
set.seed(2)  

vecteur <- rep(0,n)  

t <- 7

#Répéter l'opération afin de simuler t tours 
for (i in 1:t) {indices <- sample(seq_along(vecteur), length(vecteur) %/% 2)  # Indices aléatoires pour ajouter 1

vecteur[indices] <- vecteur[indices] + 1  # Ajouter 1 aux éléments sélectionnés

sort(vecteur)}

#Vecteur trié 
print(sort(vecteur))

#Créer le tableau des valeurs de notre simulation
tableau <- table(vecteur)

barplot(tableau, main = "Histogramme des modalités", xlab = "Nb de points", ylab = "Nb de joueurs")
