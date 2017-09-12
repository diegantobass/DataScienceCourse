# -*- coding: utf8 -*-

# Ceci est un commentaire
# Ce script reprend le travail effectué durant la séance 2

print("--- Python 101 - Séance 2 ---")
print("-----------------------------")

"""
Ceci est un autre commentaire
Il est crucial de commenter son code de façon claire et précise ! Documenter le code fait partie du code
Les commentaires entre triples guillemets et après les dièses ne sont pas executé lorsque vous lancez le script
"""

print("---- afficher un message ----")

print("Let's go") # les guillemets doubles permettent d'inclure des apostrophes dans le message
print('"Let us go"') # les simples permettent d'inclure des doubles
print('Let\'s go') # il est également possible "d'échapper" les caractères spéciaux pour que python ne les considère pas comme du code
# print('Let's go') # cette ligne de code ne fonctionnera pas (dé-commentez la et essayez de lancer le script)

print("--- déclarer des variables --")

# stocker une valeur dans une variable
variable = "Hello, World!"
print(variable)

# les types de valeur
integer = 725 # un entier
string = "Hello, World!" # un texte
float_ = 1.23 # un nombre décimal 
booleen = True # un booléen : soit "vrai", soit "faux"

print(integer) # j'affiche la valeur stockée dans la variable "integer"
print(type(integer)) # j'affiche le type de la variable integer

"""
print() et type() sont des fonctions du langage python. Elles prennent un argument entre leurs parenthèses
print() affiche sont argument dans le terminal. type() nous donne le type de sont argument
print(type(variable)) va donc afficher dans le terminal le résultat de la fonction type(variable)
les deux lignes suivantes font la même chose en deux étapes plutôt qu'une seule
"""

type_integer = type(integer)
print(type_integer)

# formater un message à afficher dans le terminal
print("J'ai affiché {} fois {} dans ma vie, c'est {}...".format(integer, string, booleen))
# dans chacunes des paires d'accolades est injecté l'une des variables de la fonction format() dans l'ordre

print("----- input utilisateur -----")

# input utilisateur
user_input = input("Combien font 2 et 2 ? ")
print("2 et 2 font {}.".format(user_input))

string_input = input("Comment t'appelles-tu ? ") # fonction input() pour python 3
# string_input = raw_input("Comment t'appelles-tu ? ") # fonction raw_input() pour python 2 car input() ne prend pas de texte dans python 2.7
print("Tu t'appelles {}.".format(string_input))

print('{} a affiché {} fois "{}" dans son terminal, c\'est un data-scientist.'.format(string_input, integer, variable)) # notez l'utilisation des guillemets

print("-- opérateurs mathématiques -- bonus")

# opérateurs mathématiques
addition = 7 + 23
subtraction = 108 - 18
multiplication = 1000 * 0.5
division = 108 / 9
puissance = 2 ** 3
modulo = 5 % 4 # le reste de la division

more = addition * subtraction # la variable contient le résultat d'une opération sur deux variables
print(more)
more = more + 4 - addition # on modifie la variable : elle est maintenant égal à son ancienne valeur plus 4 moins la valeur de addition
print(more)

print("--- les conditions avec if --- bonus")

booleen = True # on déclare un booleen avec la valeur "vrai"

if booleen == True: # si la variable booleen est égale à "vrai"
	print("sweet success") # alors j'exécute ce code

if booleen == False:
	print("epic fail") # ce code ne sera pas exécuté puisque booleen == "True"

"""
notez les deux points qui suivent la condition formulée après le 'if' -> if condition: retour à la ligne
notez l'indentation : la tabulation en début de ligne avant les instructions qui suivent la condition
ces éléments appartiennent à la syntaxe obligatoire de python, ils sont nécessaires sinon "Syntax Error"
"""

un_entier = 4 # on déclare une variable avec la valeur 4

if un_entier == 4:
	print("Ce code s'exécute car la variable un_entier est égale à 4")

print("-----------------------------")


