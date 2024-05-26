                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################

#########################################     Python Boucles     ###############################################

##### Boucle while
# loop = True
# Prenom = input("Entrez votre prenom svp!")

# while loop:
#     if Prenom:
#         print(f"Bonjour {Prenom}, comment allez vous?")
#         loop=False
#     else:
#         Prenom = input("Entrez votre prenom svp!")


##### Boucle for

# for i in range (10):
#     print((i+1)**2)
    
##### Sequence

# liste=["Nestor", 35, True, range(10)]
# print(liste)
# print(liste[0])
# for i in liste:
#     if type(i) == str:
#         print(i.upper())
#     elif type(i) == int:
#         print(i**2)
#     else:  
#         print(i)

##### Sequence
# turple=("Nestor", 35, True, range(10))
# # print(turple)
# # print(turple[0])
# for i in turple:
#     if type(i) == str:
#         print(i.upper())
#     elif type(i) == int:
#         print(i**2)
#     else:  
#         print(i)
        
plats = [
    ("Pizza", (0, 23), (10,55)),
    ("Hamburger", (7, 32), (8,42)),
    ("Riz", (0, 25), (5,65)),
]

Age = 27

for plat in plats:
    print(plat[1][0])
