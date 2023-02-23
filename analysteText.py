# Demander à l'utilisateur d'entrer le texte
texte = input("Entrez le texte à analyser : ")

# Calculer le nombre de caractères dans le texte
nb_caracteres = len(texte)

# Calculer le nombre de mots dans le texte
mots = texte.split()
nb_mots = len(mots)

# Calculer le nombre de phrases dans le texte
phrases = texte.split(".")
nb_phrases = len(phrases)

# Afficher les résultats
print("Le texte contient", nb_caracteres, "caractères,", nb_mots, "mots et", nb_phrases, "phrases.")


#Dans ce code, nous demandons à l'utilisateur d'entrer un texte, puis nous utilisons la fonction len() 
# #pour calculer le nombre de caractères dans le texte. Nous utilisons ensuite la méthode split() pour 
# #diviser le texte en mots et en phrases (en utilisant le caractère "." comme délimiteur pour les #phrases). 
# Nous calculons le nombre de mots en utilisant la fonction len() sur la liste de mots, et le 
# #nombre de phrases en utilisant la fonction len() sur la liste de phrases. Nous affichons ensuite les 
# #résultats avec un message explicatif.