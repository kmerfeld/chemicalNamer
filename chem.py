#!/usr/bin/python
import re
funcGroup = ""
finished = []
chem = raw_input("enter a string ")
def breakdown(chem):
	chemical = []
	for x in chem:
		m = re.search("^[\)\(]",chem)
		if m: 
			temp = list(chem)
			chemical.append(temp.pop(0))
			chem = "".join(temp)
		
	
		m = re.search("^[1-9=#:]",chem)
		if m:
			temp = list(chem)
			chemical.append(temp.pop(0))
			chem = "".join(temp)
			
		m = re.search('^[A-Z]', chem) 			##this tests for organic chemicals
		if m:
			n = re.search ("^.[a-z]", chem)
			if n:
				atom = []
				temp = list(chem)
				atom.append(temp.pop(0))
				atom.append(temp.pop(0))
				atomMashed = "".join(atom)
				chemical.append(atomMashed)
				chem = ''.join(temp)
			else:
				temp = list(chem) 		#take the chemicals and turn it to a list
			        chemical.append(temp.pop(0)) 	#throw the chemical onto the chemical stack
				chem = "".join(temp) 		#remake the chemical string

		m = re.search("^[\[]", chem) 			##This tests for a bracket, 
		if m: 						##A bracket means any chemical other then organic ones
								##Organic chemicals are B, C, N, O, P, S, F, Cl, Br, and i 
			temp = list(chem)
			atom = []
			atom.append(temp.pop(0))
			while atom[-1] != "]":
				atom.append(temp.pop(0))
			atomMashed = "".join(atom)
			chemical.append(atomMashed)
			chem = "".join(temp)
	return chemical

molecule = []
molecule = breakdown(chem)
print molecule


##search for the longest chain.
longest = 0
tempLong = 0
startPoint = -1
for x in molecule:
	if(x == "C"):
		tempLong += 1
	if(x != "C") or (x == "("):
		if(tempLong > longest):
			longest = tempLong
		tempLong = 0
if( tempLong > longest):
	longest = tempLong
print "the largest carbon is " 
print longest
#check for Amines
#Amines have a N
for x in molecule:
	if (x == "N"):
		print "We have an Amine"
		funcGroup += "Amine"
	##check for ether
	elif(x == "O"):
		print "Oxygen detected. could be Alcohol, aldehyde, carboxylic acid, ester, or ether"


	elif (x == "F") or ( x == "Cl") or ( x == "I"):
		print "We have a Halide"
		funcGroup +="Halide"
		
