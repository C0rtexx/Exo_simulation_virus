
#Problème: Simulation d'évolution d'une infection virale

#Vous devez créer un programme en Python pour simuler l'évolution d'une infection virale sur une population de 11 500 000 personnes 
#pendant une année (365 jours). Le modèle de simulation est basique et utilise une formule simple.

#Initialisez le nombre de personnes infectées le premier jour à 100.

#Utilisez la formule suivante pour calculer le nombre de personnes infectées chaque jour, en tenant compte des rencontres 
#quotidiennes :
#nouveau_infectes = PT * infectes_jour_precedent * (population / rencontres_par_jour)
#infectes_jour_actuel = infectes_jour_precedent + nouveau_infectes

#où PT vaut 0.01, PG vaut 0.05, et le nombre de rencontres par jour est initialement 10.

#Du jour 30 au jour 75 (inclus), pendant une période de confinement, le nombre de rencontres par jour devient 3 au lieu de 10.

#Les scientifiques doivent pouvoir entrer le numéro d'un jour (de 1 à 365), 
#et le programme affiche le nombre de personnes contaminées ce jour-là. S'ils entrent "0", le programme passe à la suite. 
#Le calcul du nombre de personnes infectées n'est effectué qu'une seule fois pour toute l'année.

#Pour obtenir plus de points :
#Affichez le nombre moyen de personnes infectées par jour et le nombre moyen de nouvelles infections par jour 
#sur l'ensemble de l'année.
#Indiquez si la population guérira complètement, sera complètement infectée ou partiellement infectée.
#Affichez le numéro du jour du premier pic du nombre de personnes infectées.


Taille_population = 11500000
année = 365
PT = 0.01
PG : 0.05
rencontres_par_jour = 10  
nb_p_rencontree =
infectes_jour_precedent 


niag = infectes_jour_precedent * (1-PG)
P_infectee = niag + (Taille_population - niag) * nb_p_rencontree * niag / Taille_population * PT 


nouveau_infectes = PT * infectes_jour_precedent * (Taille_population / rencontres_par_jour)
infectes_jour_actuel = infectes_jour_precedent + nouveau_infectes
