from sets import Set
import csv
WOCountries = Set()
SSASA = Set()

SSASA1 = set()
with open("WorldBank2012Regions.csv", "rU") as d:
	CountriesReader = csv.reader(d)
	for row in CountriesReader:
		if row[2] == 'Sub-Saharan Africa':
			SSASA1.add(row[1])

with open("WorldBank2012Regions.csv", "rU") as y:
	CountriesReader = csv.reader(y)
	for row in CountriesReader:
		if row[2] == 'South Asia':
			SSASA1.add(row[1])






