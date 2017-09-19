# Python for Data-Science : Projet personnel

### Choisir un dataset

Choisissez des données sur lesquelles vous aller travailler durant les 3 prochaines séances de cours. Ces données doivent être dans __un tableur__ avec un enregistrement par ligne. Le tableur devra être au __format CSV__. Excel peut importer et exporter un classeur au format CSV [comme ceci](https://support.office.com/en-us/article/Import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba)

### Reproduire le code présenter en séance 1

À l'aide de la séance 3 du cours, tentez de reproduire les lignes de code présentées en première séance sur vos données

~~~python
import csv

mon_csv = csv.reader(open('fichier.csv', 'r'))
output = csv.writer(open('sortie.csv', 'w'))

for line in mon_csv:
    colonne_2 = line[1]
    colonne_3 = line[2]
    new_colonne = colonne_2 + colonne_3

    new_line = line + [new_colonne]
    output.writerow(new_line)
~~~

### Ne pas hésiter à poser des questions

Au professeur, à Google, ou directement à Stack Overflow.
