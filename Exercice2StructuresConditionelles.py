                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################

#########################################     Python Structures Conditionnelles     ##########################################


###### Exercice 2
Prenom= input("Entrer votre prenom :")
Age= input("Entrer votre age :")
Sage= input("Entrer 1 si vous avez ete sage et 0 sinon :")
Chaine1 = f"Felicitation {Prenom} !!!!! vous avez été sage cette annee et le père Noël attend impatiemment votre lettre de voeux"
Chaine2 = f"Désolé  {Prenom} !!!!! vous avez été vilain cette annannée et le père Noël n’est pas du tout content de vous"

if int(Age)<=10 and bool(int(Sage)) == True:
    print(Chaine1)
elif int(Age)<=10 and bool(int(Sage)) == False:
    print(Chaine2)
elif int(Age)>10 :
    print("Vous n'etes pas eligible!")