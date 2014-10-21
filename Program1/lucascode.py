#Programming Assignment 1
#Lucas Churchman

import csv
import sets

WOCountries = set()
Countries = set()

#Task 1: Create the sets
with open("WorldBank2012DataWORegions.csv", "rU") as f:
	WOCountriesReader = csv.reader(f)
	for row in WOCountriesReader:
		WOCountries.add(row[1])

with open("WorldBank2012Regions.csv", "rU") as d:
	CountriesReader = csv.reader(d)
	for row in CountriesReader:
		Countries.add(row[1])

if WOCountries == Countries:
	print 'Success!'
	
else:
#Task 2: Which is superset
	print 'Sets do not match'
	print ' '
	if WOCountries >= Countries == True:
		print 'WOCountries is the superset'
	else:
		print'Countries is the superset'
	print ' '
#Task 2: difference of the sets
	print 'Here are the codes that are not contained in both sets:'
	uncommonCodes = WOCountries - Countries
	print uncommonCodes
	print ' '
#Task 3: Codes in both sets
	print 'Here are the codes contained by both sets:'
	commonCodes = WOCountries.intersection(Countries)
	print commonCodes
	print ' '

#Task 4: Create set for Region Codes
RegionCodes = set()
with open("WorldBank2012Regions.csv", "rU") as g:
	RegionCodesReader = csv.reader(g)
	for row in RegionCodesReader:
		RegionCodes.add(row[1])
print ' '

#Task 5: Check if RegionCodes is a partition for the intersection of the two previous sets	
commonCodes = WOCountries.intersection(Countries) #WOCountries(intersect)Countries
	#Part 1: Check that the set is not empty (P!=0)
if len(RegionCodes)!= 0: 
	print 'Set ''regionCodes'' is not empty: PASS!'
else: 
	print 'Set ''regionCodes''  is empty: failure'
	#Part 2: Check to see if the union of RegionCodes and commonCodes is equal
if commonCodes == RegionCodes:
	print 'The union of the sets are equal: PASS!'
else:
	print 'The union of the sets are not equal: failure'
if commonCodes.intersection(RegionCodes) != 0:
	print 'The intersection of the sets is empty: PASS!'
else:
	print 'There are common elements in one or more of the sets in the partition: failure'
print ' '
print 'If all 3 tests are passed, then RegionCodes is a valid partition'
print 'of the intersection of WoCountries and Countries!'
print ' '

#Task 6: Generate a set of countries and Sub-Saharan Africa and South Asia from the set of countries in WOCOuntries and Countries
SahSA = set()
with open("WorldBank2012Regions.csv", "rU") as d:
	CountriesReader = csv.reader(d)
	for row in CountriesReader:
		if row[2] == 'Sub-Saharan Africa':
			SahSA.add(row[1])
with open("WorldBank2012Regions.csv", "rU") as y:
	CountriesReader = csv.reader(y)
	for row in CountriesReader:
		if row[2] == 'South Asia':
			SahSA.add(row[1])

SSASA = SahSA.intersection(commonCodes)

arableLand = set()
#Task 7: Generate a set of countries with >10% of arable land
with open("WorldBank2012DataWORegions.csv", "rU") as q:
	CountriesReader = csv.reader(q)
	for row in CountriesReader:
		if row[2] == 'Arable land (% of land area)' and row[4] > 10:
			arableLand.add(row[1])
ArableLand = arableLand.intersection(commonCodes)

#Task 8: Intersection of SSASA and ArableLand

SSASAintAL =ArableLand.intersection(SSASA)
print 'Countries in the Sahara or South Asia with >10% arable land:'
print SSASAintAL
	
			
