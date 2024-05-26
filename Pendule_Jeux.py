                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################
"""

Ce projet est un jeux qui permet de trouver un mot cache selectionne dans un dictionnaire. Il est dynamique en ce sens qu'il vous guide

a chaque fois pour vous rappocher du mot cache. Le score et le nombre de tentative du joueur 

lui sont donnes a la fin.

"""
NB_CHANCE = 10

dictionnaire = [
    "test",
    "vie",
    "aimer",
    "secret",
    "mysterieux",
    "cacher"
]
mot = dictionnaire[3]
mot_len = len(mot)
essaie = 1
score = 100
mystere = ""

loop = True

for i in range(mot_len):
    
    if i%2 ==0:
        
        mystere += mot[i]
        
    else:
        
        mystere += "*"

      
while loop:
    
    print(mystere)
    mot_utilisateur = input(f"Quel est le mot caché?")
    
    if essaie <= NB_CHANCE:
    
        if not len(mot_utilisateur) == mot_len:
            
            print(f"Desole vous devez entrer un mot contenant {mot_len} caracteres")
            essaie +=1
            score -=10
            
        else:
            
            if mot_utilisateur != mot:
                
                mystere_backup = mystere
                mystere = ""
                
                for i in range(mot_len):
                    
                    if mot_utilisateur[i] == mot[i]:
                        if i > 0:
                            if mot[i-1] == mot_utilisateur[i-1]:
                                mystere += mot[i]
                            else:
                                mystere += mystere_backup[i]      
                        else:
                            mystere += mystere_backup[i]
                            
                    else:
                        
                        mystere += mystere_backup[i]
                print(f"Desolé!!!! vous avez manque le mot caché. Essayez a nouveau")
                essaie +=1
                score -=10
                
            else:
                
                loop = False
                print(f"Felicitation!!! Vous avez trouve le mot cache : {mot}")
                essaie +=1
                score -=10
    else:
                
        loop = False
        print(f"Voua avez manque le mot cache. Il est  {mot}")
        print(f"Nombre d'essais : {essaie} \nScore : {score}")