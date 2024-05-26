                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################
"""

Ce projet est un jeux qui permet de trouver un nombre magic aleatoirement choisie par le systeme. 

Ceci se fait a travers une sucession de comparaisons. Il est dynamique en ce sens qu'il vous guide

a chaque fois pour vous rappocher du nombre magique. Le score et le nombre de tentative du joueur 

lui sont donnes a la fin.

"""
# Importons les modules utiles a notre programme
import random

# Definition des Constantes
NB_CHANCE = 10

# Definissons les variables
val_min = 10 

val_max = 100

mystere = 23#random.randint(val_min, val_max)

essaie = 1

score = 100

loop = True

while loop:
    
    valeur_utilisateur = input(f"Veillez entrer un nombre compris entre {val_min} et {val_max}  ")
    valeur_int = int(valeur_utilisateur)
    
           
    if essaie <= NB_CHANCE:
            
            if valeur_int >= val_min and valeur_int <= val_max:
                    
                if valeur_int > mystere:
                    
                    print("Plus grand que le nombre mystere")
                    essaie +=1
                    score -=10
                    
                elif valeur_int < mystere:
                    
                    print("Plus petit que le nombre mystere")
                    essaie +=1
                    score -=10
                    
                else:
                    
                    print(f"Felicitations!!!!!!!! \nVous avez trouve le nombre magique. Il est de {valeur_int}")
                    print(f"Nombre d'essais : {essaie} \nScore : {score}")
                    loop = False
            else:
                print("La valeur choisie n'est pas conforme aux exigences.")
                essaie +=1
                score -=10
    else:
                
        loop = False
        print(f"Voua avez manque le nombre mystere. Il est de {mystere}")
        print(f"Nombre d'essais : {essaie} \nScore : {score}")
                    
    

            
        