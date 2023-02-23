# Demander à l'utilisateur d'entrer deux nombres
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))

# Demander à l'utilisateur de choisir une opération
print("Veuillez choisir une opération -\n1. Addition\n2. Soustraction\n3. Multiplication\n4. Division")
choix = int(input("Entrez votre choix (1/2/3/4) : "))

# Effectuer l'opération en fonction du choix de l'utilisateur
if choix == 1:
    resultat = num1 + num2
    print(num1, "+", num2, "=", resultat)
    
elif choix == 2:
    resultat = num1 - num2
    print(num1, "-", num2, "=", resultat)

elif choix == 3:
    resultat = num1 * num2
    print(num1, "*", num2, "=", resultat)

elif choix == 4:
    if num2 == 0:
        print("Erreur : division par zéro n'est pas possible")
    else:
        resultat = num1 / num2
        print(num1, "/", num2, "=", resultat)
else:
    print("Erreur : choix invalide")

# Dans ce code, nous demandons
# à l'utilisateur d'entrer deux nombres,
# puis de choisir une opération
# (1 pour l'addition, 2 pour la soustraction, 3 pour la multiplication et 4 pour la division)
# Nous utilisons ensuite une série de conditions 
# "if-elif-else" pour effectuer l'opération en fonction du choix
#                                                                                                    de l'utilisateur et afficher le résultat correspondant.