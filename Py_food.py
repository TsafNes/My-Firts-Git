                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################

#########################################     Projet 1     ###############################################
"""
Ce projet permet a un utilisateur de rentrer son age et un menu lui sera propose en fonction de son age age et
de l'heure autorisee a prendre ce menu. Dans le menu on retrouve divers plat et diverses boissons.

Pour cela on utilse les tuples, les listes pour les plats et boissons selon la structure suivante:

Boisson = [(Nom, Age_min)]
Plats = [(Nom, (Heure_min, Heure_max), Age_min)]
"""

# plats = [
#     ("Pizza", (0, 23), 10),
#     ("Hamburger", (7, 22), 8),
#     ("Riz", (0, 23), 5),
#     ("Spaguetti", (11, 19), 0),
#     ("Salade de fruits", (0, 23), 0),
#     ("Salade simple", (15, 23), 4),
    
#     ("Cafe", (6, 16), 16),
#     ("Nexpresso", (6, 14), 19),
#     ("Capucino", (6, 16), 16),
#     ("The", (15, 22), 10),
    
#     ("Soupe au legume", (18, 23), 0),
#     ("Soupoe au poulet", (17, 21), 10),
#     ("Soupe de beouf", (16, 20), 8),
#     ("Soupe de poisson", (15, 22), 10),
# ]

# Boissons = [
#     ("Coca Cola", 10),
#     ("LAit", 0),
#     ("Jus naturel d'orange", 5),
#     ("Jus naturel de mangue", 15),
#     ("Jus naturel d'ananas", 8),
#     ("Sprite", 10),
#     ("Jack Daniel", 20),
#     ("Coureur des bois", 23),
#     ("Champagne", 19),
# ]

# Age = input("Svp veillez saisir votre age!")
# Heure = input("Svp quelle heure est-il?")

# print()

# print("-------------------------- Le menu du jour --------------------------")

# for Plat in plats:
#     if int(Age)>=Plat[2]:
#         print(Plat[0])

# print()

# print("-------------------------- Les boissons disponible --------------------------")


# for Boisson in Boissons:
#     if int(Age)>=Boisson[1]:
#         print(Boisson[0])
        
        
        

#########################################     Projet 2     ###############################################
"""
Ce projet permet a un utilisateur de rentrer son age et un menu lui sera propose en fonction de son age age et
de l'heure autorisee a prendre ce menu. Dans le menu on retrouve divers plat et diverses boissons.

Pour cela on utilse les tuples, les listes pour les plats et boissons selon la structure suivante:

Boisson = [(Nom, (Age_min,Age_max))]
Plats = [(Nom, (Heure_min, Heure_max), (Age_min,Age_max))]
"""



plats = [
    ("Pizza", (0, 23), (10,55)),
    ("Hamburger", (7, 22), (8,42)),
    ("Riz", (0, 23), (5,65)),
    ("Spaguetti", (11, 19), (0,46)),
    ("Salade de fruits", (0, 23), (0,47)),
    ("Salade simple", (15, 23), (4,29)),
    
    ("Cafe", (6, 16), (16,64)),
    ("Nexpresso", (6, 14), (19,28)),
    ("Capucino", (6, 16), (16,50)),
    ("The", (15, 22), (10,85)),
    
    ("Soupe au legume", (18, 23), (0,46)),
    ("Soupoe au poulet", (17, 21), (10,34)),
    ("Soupe de beouf", (16, 20), (8,40)),
    ("Soupe de poisson", (15, 22), (10,62)),
]

Boissons = [
    ("Coca Cola", (10,39)),
    ("LAit", (0,90)),
    ("Jus naturel d'orange", (5,87)),
    ("Jus naturel de mangue", (15,75)),
    ("Jus naturel d'ananas", (8,67)),
    ("Sprite", (10,62)),
    ("Jack Daniel", (20,43)),
    ("Coureur des bois", (23,75)),
    ("Champagne", (19,46)),
]

Age = input("Svp veillez saisir votre age!")
Heure = input("Svp quelle heure est-il?")

print()

print("-------------------------- Le menu du jour --------------------------")
# Plats = [(Nom, (Heure_min, Heure_max), (Age_min,Age_max))]
for Plat in plats:
    if int(Age)<=Plat[2][1] and int(Age)>=Plat[2][0]:
        print(Plat[0])
        
        
print()

print("-------------------------- Les boissons disponible --------------------------")

# Boisson = [(Nom, (Age_min, Age_max)]
for Boisson in Boissons:
    if int(Age)<=Boisson[1][1] and int(Age)>=Boisson[1][0]:
        print(Boisson[0])

