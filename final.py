# -*- coding: utf8 -*-

import csv

mon_csv = csv.reader(open('associations.csv', 'r'))
headers = mon_csv.next()

sortie = csv.writer(open('sortie.csv', 'w'))
sortie.writerow(headers)

for line in mon_csv:
	code_postal = line[11].strip()
	if code_postal == "75018":
		print("{} est dans mon arrondissement".format(line[2]))
		sortie.writerow(line)
