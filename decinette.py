import random

# Générer un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

# Initialiser le compteur d'essais
compteur = 0

# Demander à l'utilisateur de deviner le nombre
while True:
    devinette = int(input("Devinez le nombre (entre 1 et 100) : "))
    compteur += 1
    
    # Vérifier si la devinette est correcte
    if devinette == nombre_secret:
        print("Bravo, vous avez trouvé le nombre en", compteur, "essais !")
        break
        
    # Donner des indices pour aider l'utilisateur
    elif devinette < nombre_secret:
        print("Le nombre est plus grand que", devinette)
    else:
        print("Le nombre est plus petit que", devinette)


# Voici un exemple de code Python pour créer un jeu de devinette où l'ordinateur choisit un nombre aléatoire et l'utilisateur doit le deviner. L'ordinateur donne des indices pour aider l'utilisateur à trouver le nombre :

python
Copy code
import random

# Générer un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

# Initialiser le compteur d'essais
compteur = 0

# Demander à l'utilisateur de deviner le nombre
while True:
    devinette = int(input("Devinez le nombre (entre 1 et 100) : "))
    compteur += 1
    
    # Vérifier si la devinette est correcte
    if devinette == nombre_secret:
        print("Bravo, vous avez trouvé le nombre en", compteur, "essais !")
        break
        
    # Donner des indices pour aider l'utilisateur
    elif devinette < nombre_secret:
        print("Le nombre est plus grand que", devinette)
    else:
        print("Le nombre est plus petit que", devinette)
        
        
# Dans ce code, nous importons le module random pour générer 
# un nombre aléatoire entre 1 et 100. 
# Nous initialisons également un compteur pour suivre le nombre d'essais 
# que l'utilisateur a effectués. Nous demandons ensuite à l'utilisateur de deviner le nombre en utilisant une boucle while. 
# À chaque essai, nous vérifions si la devinette de l'utilisateur est correcte. 
# Si c'est le cas, nous affichons un message de félicitations et le nombre d'essais 
# effectués, puis nous sortons de la boucle while à l'aide de l'instruction break. 
# Si la devinette de l'utilisateur est incorrecte, nous donnons des indices pour aider l'utilisateur 
# (en indiquant si le nombre à deviner est plus grand ou plus petit que la devinette de l'utilisateur),
# puis nous demandons une nouvelle devinette à l'utilisateur dans la boucle while.