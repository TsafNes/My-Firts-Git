                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################

#########################################     Python Structures Conditionnelles     ##########################################


###### Exercice 1
Age= input("Entrer votre age :")
if int(Age)>=50:
    print("Vous etes Aîné et avez acces a des filmes romantiques!")
elif 19<=int(Age)<50:
    print("Vous etes Adulte et avez acces a des contenus avances!")
elif 13<=int(Age)<18:
    print("Vous etes Adolescent et avez acces a des Mangas et des filmes comiques!")
elif 6<=int(Age)<12:
    print("Vous etes Enfants et avez acces a desvcartes et des dessins animes!")
else:
    print("Vous etes Bebe et avez acces a des berceuses!")