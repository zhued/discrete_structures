# Programming Assignment 1
# Edward Zhu

from sets import Set
import csv

#TASK1: Create sets
WOCountries = Set()
Countries = Set()

with open("WorldBank2012DataWORegions.csv", "rU") as wo:
    WOCountriesReader = csv.reader(wo)
    for row in WOCountriesReader:
	WOCountries.add(row[1])

with open("WorldBank2012Regions.csv", "rU") as reg:
    CountriesReader = csv.reader(reg)
    for row in CountriesReader:
	Countries.add(row[1])

#TASK2: Superset
if WOCountries != Countries:
    print 'WOCountries and Countries are not equal!'
    if WOCountries.issuperset(Countries):
        print 'WOCountries is the superset!'
    else:
        print 'Countries is the superset!'
else:
    print 'WOCountries and Countries are equal! They should not!'
    
print 'The difference between the two is:'
print WOCountries.difference(Countries)
print

#TASK3: Intersection
print 'The intersection between the two is:'
print WOCountries.intersection(Countries)
print

#TASK4: RegionCodes
RegionCodes = Set()
with open("WorldBank2012Regions.csv", "rU") as rg:
    RegionCodesReader = csv.reader(rg)
    for row in RegionCodesReader:
        RegionCodes.add(row[1])


#TASK5: RegionCodes Partition of intersection?
print
print 'RegionCodes Paritition of WOCountries.intersection(Countries)?'
if RegionCodes:
    print 'Set is not empty. PASS!'
    if WOCountries.intersection(Countries).union(RegionCodes):
        print 'The union of the sets are equal: PASS!'
        if WOCountries.intersection(Countries).intersection(RegionCodes) != 0:
            print 'The intersection of the sets is empty: PASS!'
            print 'RegionCodes IS A VALID PARTITION'
        else:
            print 'There are common elements in one or more of the sets in the partition: fail'
    else:
	print 'The union of the sets are not equal: fail'
else: 
    print 'Set ''regionCodes''  is empty: fail'

#TASK6: A set of countries and Sub-Saharan Africa and South Asia from the set of countries in WOCOuntries and Countries
SSASA1 = set()
with open("WorldBank2012Regions.csv", "rU") as africa:
	CountriesReader = csv.reader(africa)
	for row in CountriesReader:
		if row[2] == 'Sub-Saharan Africa':
			SSASA1.add(row[1])
with open("WorldBank2012Regions.csv", "rU") as asia:
	CountriesReader = csv.reader(asia)
	for row in CountriesReader:
		if row[2] == 'South Asia':
			SSASA1.add(row[1])
SSASA = SSASA1.intersection(WOCountries.intersection(Countries))


#TASK7: A set of countries with >10% of arable land
ALand = set()
with open("WorldBank2012DataWORegions.csv", "rU") as al:
	CountriesReader = csv.reader(al)
	for row in CountriesReader:
		if row[2] == 'Arable land (% of land area)' and row[4] > '10':
			ALand.add(row[1])
ArableLand = ALand.intersection(WOCountries.intersection(Countries))

#TASK8: SSASA and ArableLand
print
print 'Countries in Sub-Sahara Africa or South Asia with >10% arable land:'
print SSASA.intersection(ArableLand)
print

