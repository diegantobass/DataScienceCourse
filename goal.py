import csv

mon_csv = csv.reader(open('mock.csv', 'r'))
output = csv.writer(open('output.csv', 'w'))
headers = next(mon_csv)

for line in mon_csv:
    colonne_1, colonne_2, colonne_3, colonne_4, colonne_5, colonne_6 = line
    colonne_plus = colonne_2 + colonne_3

    new_line = line + [colonne_plus]
    output.writerow(new_line)

print("I am data-scientist. I am a data-scientist. I am a data-scientist.")