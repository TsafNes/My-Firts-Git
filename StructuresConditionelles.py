                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################

#########################################     Python Structures Conditionnelles     ##########################################

##### Structure if-else
Age = input("Entrez votre age: ")


if Age>=18:
    print("Vous etes majeur!")
else:
    print("Vous etes mineur !")
    
##### Structure if-elif-else
Age = input("Entrez votre age: ")

if int(Age)>=65:
    print("Vous etes Aîné!")
elif 25<=int(Age)<65:
    print("Vous etes Adulte !")
elif 15<=int(Age)<24:
    print("Vous etes Adolescent !")
elif 5<=int(Age)<14:
    print("Vous etes Enfants !")
else:
    print("Vous etes Bebe !")

