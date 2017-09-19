# -*- coding: utf8 -*-

print("--- Python 101 - Séance 3 ---")
print("-----------------------------")

# Revisions
print("--- Révisions -")

print('Let\'s go')
nom = input("Comment t'appelles-tu ? ")
print('Let\'s go go {}'.format(nom))
print("Ceci est un integer : {}".format(4))
print("Ceci est un float : {}".format(4.465))
print("Ceci est un booléen : {}".format(True))

# opérateurs mathématiques
print("--- Opérateurs mathématiques -")
addition = 7 + 23
subtraction = 108 - 18
multiplication = 1000 * 0.5 # les floats s'écrivent avec un point
division = 108 / 9 # produit toujours un float
puissance = 2 ** 3
modulo = 5 % 4 # le reste de la division

more = addition * subtraction
print(more)
more = more + 4 - addition # la variable more prend l'ancienne valeur de more + 4 - 30
print(more)

"""
Le sens de lecture du code est important : haut - bas - gauche - droite
Le code est interprété dans l'ordre de lecture
"""

# conditions avec if
print("--- Conditions avec if - ")

booleen = True # on déclare un booleen avec la valeur "vrai"

if booleen == True: # si la variable booleen est égale à "vrai"
	print("Ce code s'exécute car la condition est vraie")

if booleen == False:
	print("Ce code ne s'exécute pas car la condition est fausse, booleen est égal à True")

un_entier = 4 # on déclare une variable avec la valeur 4
if un_entier == 4:
	print("Ce code s'exécute car la variable un_entier est égale à 4")

"""
L'indentation (la tabulation en début de ligne) avant les instructions qui suivent une condition if sont cruciales
Elle indique la structure du code et dénote que le bloc de code qui suit le if est contenu dans cette condition
Une erreur explicite sera renvoyée dans le terminal (IndentationError) si l'indentation n'est pas correcte
Les lignes vide ne sont pas importante en revanche, elles facilitent seulement la lecture humaine
"""

# opérateurs logiques
print("--- Opérateurs logiques - ")

if un_entier < 5:
	print('un_entier est inférieur à 5')

if un_entier >= 4:
	print('un_entier est supérieur ou égal à 4')

if True != False:
	print('la valeur booléenne True n\'est pas égale à False')

if (True == True) and (un_entier < 10):
	print('les conditions complexes doivent être organisées grâce à des parenthèses !')


# listes
print("--- Listes -")
liste = [0, 1, 2, 3, 65, 1, 42]
print(liste)
premier_element = liste[0]
deuxieme_element = liste[1]
dernier_element = liste[6]
print("Le premier élément est {}, attention il a l'indice 0".format(premier_element))

negatif = liste[-4] # indice négatif, depuis la fin
slices_1 = liste[0:4] # élements avec indices de 0 à 4
slices_2 = liste[1:] # depuis l'indice 1 jusqu'à la fin
slices_3 = liste[:-1] # I don't even...
slices_4 = liste[::-1] # ...

# strings are lists
print("--- Strings are lists -")
text = "incroyable ce texte est très intéressant"
c = text[2]
c_slices = text[:10]
print("J'imprime les 10 premiers élement de la variable text : {}".format(c_slices))

# methodes len()
print("--- Méthodes -")
longueur_text = len(text)
longueur_liste = len(liste)
print("Le texte contenu dans la variable text fait {} caractères".format(longueur_text))

# méthodes de string
majuscules = text.upper() # upper() passe tout le texte en majuscules
minuscules = majuscules.lower() # lower() passe tout en minuscules
# parfois, il faut consulter la documentation de python... https://docs.python.org/3.6/library/string.html

# boucle for
print("--- Boucle for -")
print(liste)

for element in liste: # pour chaque élément dans la liste
	print(element) # j'exécute cette opération

# ouvrir un fichier
fichier = open('DataScienceCourse/mock.csv', 'r') # la fonction open() ouvre un fichier

"""
La fonction open() prend 2 arguments. Le premier est le nom du fichier.
Le fichier doit être sauvegardé dans le même dossier que votre script.
Le second argument est le mode d'ouverture du fichier. r pour read.
"""

print(fichier) # affiche l'objet python qui contient mon fichier prêt à être lu
# for line in fichier: # pour le lire j'utilise une boucle -> pour chaque line de mon fichier
# 	print(line)	# j'affiche la ligne

"""
Le fichier que nous lisons n'est pas un fichier texte classique, c'est un tableur au format csv
Pour le lire correctement est préservé sa structure en ligne et en cases, il nous faut des méthodes adaptées
Dans python, le paquet csv contient les méthodes adaptées à la lecture des fichiers csv
"""

# importer un paquet
print("--- importer un paquet -")
import csv # j'importe le paquet csv dont la documentation est là : https://docs.python.org/2/library/csv.html

mon_csv = csv.reader(fichier) # le paquet csv permet la création d'un reader(), un liseur de fichier csv
print(mon_csv) # affiche l'objet python prêt à lire le csv

for line in mon_csv: # pour chaque line du csv
	print(line) # j'affiche la line

######################
# et le code présenté en séance un est enfin compréhensible !

import csv

mon_csv = csv.reader(open('DataScienceCourse/mock.csv', 'r'))
output = csv.writer(open('sortie.csv', 'w')) # w pour write, c'est le fichier de sortie

for line in mon_csv:
    colonne_1, colonne_2, colonne_3, colonne_4, colonne_5, colonne_6 = line # chaque variable a la valeur d'un élement de la liste
    colonne_7 = colonne_2 + colonne_3

    new_line = line + [colonne_7] # j'ajoute la liste [colonne_7] à la liste line
    output.writerow(new_line)

print("I am data-scientist. I am a data-scientist. I am a data-scientist.")

