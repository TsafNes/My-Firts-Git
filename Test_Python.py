#########################################     Formatage de texte     ##########################################

Nom = "Tsafack"
Prenom = "Nestor "
Nom_Complet = Prenom + Nom
Age = 35

#################  Formatage avec operateur d'addition ################# 

#print(Nom_Complet)

#print(Prenom + Nom) 

#print(Prenom,Nom)

#print("Je m'appelle", Nom_Complet, "et j'ai", Age, "ans")

#print("Hello, Je m'appelle " + Nom_Complet + " et j'ai " + str(Age) + " ans")

############### Formatage avec le symbole % #####################
#print("Bonjour, je m'apelle %s %s et j'ai %d ans" %(Prenom, Nom, Age))
# Chaine1 = "Bonjour, je m'apelle %s %s et j'ai %d ans" %(Prenom, Nom, Age)
#print(Chaine1)  

############### Formatage avec la fonction format #####################
Chaine2 = "Bonjour, je m'apelle {} {} et j'ai {} ans" .format(Prenom, Nom, Age)
Chaine3 = "Bonjour, je m'apelle {0} {1} et j'ai {2} ans" .format(Prenom, Nom, Age)
Chaine4 = "Bonjour, je m'apelle {p} {n} et j'ai {a} ans" .format(a=Age, p=Prenom, n=Nom) #Meilleure methode de formatage de 
#print(Chaine2)
#print(Chaine3)
#print(Chaine4)

############### Formatage avec f string #####################
Chaine5 = f"Bonjour, je m'apelle {Prenom} {Nom} et j'ai {Age} ans" #Encore plus Meilleure methode de formatage
print(Chaine5)
