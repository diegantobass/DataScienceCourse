# -*- coding: utf8 -*-

# Ceci est un commentaire, il est précédé d'un dièse
# Ce script reprend le travail effectué durant la séance 1 et 2 du cours de Python : Data Science for Dummies
print("--- Python - Data Science for Dummies ---")
print("-----------------------------------------")
"""
Il est crucial de commenter de façon claire et précise ! Documenter le code fait partie du code
Les commentaires entre triples guillemets permettent de commenter sur plusieurs lignes.
"""

###

print("--- afficher un message ---")
print("Let's go") # les guillemets doubles permettent d'inclure des apostrophes dans le message
print('Let "us" go') # les simples permettent d'inclure des doubles
print('Let\'s go') # il est également possible "d'échapper" les caractères spéciaux pour qu'ils ne soient pas considérér comme du code
# print('Let's go') # cette ligne de code ne fonctionnera pas (dé-commentez la et essayez de lancer le script)

###

print("--- déclarer des variables ---")
variable = "Hello, World!" # stocker une valeur dans une variable
print(variable)

###

print("--- les types de variables ---")
integer = 725 # un nombre entier, integer
string = "Hello, World!" # une chaîne de caractère, string
floatnumber = 1.23 # un nombre décimal, float
booleen = True # un booléen : soit "vrai", soit "faux", boolean
rien = None # l'absence de valeur, none

print(floatnumber) # j'affiche la valeur stockée dans la variable "floatnumber"
print(type(floatnumber)) # j'affiche le type de la variable floatnumber

"""
print() et type() sont des fonctions du langage python. Elles prennent un argument entre leurs parenthèses
print() affiche sont argument dans le terminal. type() renvoie le type de sont argument
print(type(variable)) va donc afficher dans le terminal ce que renvoie (le resultat de) la fonction type(variable)
les deux lignes suivantes font la même chose en deux étapes plutôt qu'une seule
"""

type_integer = type(integer)
print(type_integer)

###

print("--- les opérateurs mathématiques ---")
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

###

print("--- les conditions avec if ---")
booleen = True # on déclare un booleen avec la valeur "vrai"

if booleen == True: # si la variable booleen est égale à "vrai"
	print("sweet success") # alors j'exécute ce code

if subtraction == 18: # si la variable booleen est égale à "faux"
	print("epic fail") # alors j'execute ce bloc de code

else: # sinon j'execute le code suivant
	print("whatever")

"""
notez les deux points qui suivent la condition formulée après le 'if' -> if condition: retour à la ligne
notez l'indentation : la tabulation en début de ligne avant les instructions qui suivent la condition
ces éléments appartiennent à la syntaxe obligatoire de python, ils sont nécessaires sinon "Syntax Error"
"""

###

print("--- toujours plus de conditions ---")
un_entier = 4 # on déclare une variable avec la valeur 4
un_booleen = True # on déclare une variable booléenne à True

# voici un bloc de conditions complet if/elif/else
if un_entier == 4:
	print("Ce code s'exécute si la variable un_entier est égale à 4")
elif un_entier < 4:
	print("Ce code s'exécute si la variable un_entier n'est pas égale à 4 et qu'elle est inférieure à 4")
else:
	print("Ce code s'exécute si ni la condition if, ni la condition elif n'a été remplie")

# il est possible d'imbriquer des conditions
if un_entier == 4:
	print("un_entier est égale à quatre")
	if un_booleen == True:
		un_entier = 5
	# si un entier est égale à 4 et que le booleen est égale à True alors je change un_entier à 5
elif un_entier == 5:
	print("un_entier est égale à cinq")


# il est aussi possible de construire des conditions complexes
if (un_entier) == 4 and (un_booleen == True):
	print("whatever")

"""
les conditions se combinent avec "and" ou "or", l'évaluation de la valeur de vérité de la condition est
alors soumise aux mêmes règles qu'en logique mathématiques. Je vous laisse le plaisir de vous confronter
aux tables de vérités des connecteurs "and" et "or" que vous avez très certainement déjà vu en terminale
"""

###

print("--- formater un message à afficher ---")
integer = 45
string = "Hello, World!"
booleen = True
print("J'ai affiché {} fois {} dans ma vie, c'est {}...".format(integer, string, booleen))
# dans chacunes des paires d'accolades est injecté l'une des variables de la fonction format() dans l'ordre

###

print("----- input utilisateur -----")
user_input = input("Combien font 2 et 2 ? ") # on demande un input à l'utilisateur qui doit y répondre pour que le code continue
print("2 et 2 font {}.".format(user_input))

string_input = input("Comment t'appelles-tu ? ") # on pose une question à l'utilisateur dont on stocke le résultat dans une variable
print("Tu t'appelles {}.".format(string_input))

print('{} a affiché {} fois "{}" dans son terminal, c\'est un data-scientist.'.format(string_input, integer, variable)) # notez l'utilisation des guillemets

###

# Il est possible de combiner les conditions, l'input() et la fonction format() pour créer le petit programme suivant

fav_dish = input("Quel est votre plat préféré ?")
if fav_dish == "le poulet" or fav_dish == "la volaille":
	print("{} est une viande maigre")
else:
	print("Je ne connais pas {}, désolé.")

