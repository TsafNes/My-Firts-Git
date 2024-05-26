age = input("SVP entrer votre age pour afficher le contenu qui vous est adapté selon votre age!")
Age=int(age)

Contenus = [
    ("Rackaby Baby", "Unknown", 0),
    ("Eighties Baby", "Jamy Jams", 0),
    ("Babies go Beatles", "Unknown", 0),
    ("Le voyage de Chiyiro", "Miyazaki", 1),
    ("Le roi Lion", "Roger Aller", 1),
    ("Aladin", "John Musker", 1),
    ("Eat good", "Unknown", 1),
    ("One piece", "Oda", 2),
    ("Death Notes", "Oba", 2),
    ("Calm Down", "Unknown", 2),
    ("Fullmetal Alchemist", "Arakawa", 2), 
    ("OSS 117", "Michel", 2),
    ("The descent", "Marshall", 4),
    ("Medecin sans frontieres", "Unknown", 4),
    ("La ligne rouge", "Malik", 4),
    ("Voyage au bout de l'enfer", "Cimino", 4),
    ("Persuasion", "Carries", 3),
    ("Le lion de la foret", "Unknown", 3),
    ("Book of love", "Mayor", 3)
]

if 0 <= Age <= 5:   #Bebe 0 
    print("Bienvenu dans l'interface Bebe!\n\n----------------------Le contenu qui vous est adapté selon votre age:----------------------\n\n")
    for item in Contenus:
        if item[2] <= 0:
            if not item[1] == "Unknown":
                print(f"{item[0]} de {item[1]}")
            else:
                print(f"{item[0]}")
elif 6 <= Age <= 12:   #Enfant 1
    print("Bienvenu dans l'interface Enfant!\n\n----------------------Le contenu qui vous est adapté selon votre age:----------------------\n\n")
    for item in Contenus:
        if item[2] <= 1:
            if not item[1] == "Unknown":
                print(f"{item[0]} de {item[1]}")
            else:
                print(f"{item[0]}")
elif 13 <= Age <= 18:   #Ado 1
    print("Bienvenu dans l'interface Ado!\n\n----------------------Le contenu qui vous est adapté selon votre age:----------------------\n\n")
    for item in Contenus:
        if item[2] <= 2:
            if not item[1] == "Unknown":
                print(f"{item[0]} de {item[1]}")
            else:
                print(f"{item[0]}")
elif 19 <= Age <= 50:   #Adulte 1
    print("Bienvenu dans l'interface Adulte!\n\n----------------------Le contenu qui vous est adapté selon votre age:----------------------\n\n")
    for item in Contenus:
        if item[2] <= 4:
            if not item[1] == "Unknown":
                print(f"{item[0]} de {item[1]}")
            else:
                print(f"{item[0]}")
else: #Senior
    print("Bienvenu dans l'interface Senior!\n\n----------------------Le contenu qui vous est adapté selon votre age:----------------------\n\n")
    for item in Contenus:
        if item[2] <= 3:
            if not item[1] == "Unknown":
                print(f"{item[0]} de {item[1]}")
            else:
                print(f"{item[0]}")

