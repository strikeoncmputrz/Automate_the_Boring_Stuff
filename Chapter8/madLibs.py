#! python3
#  madlibs.py reads in a text file and asks the user to replace all occurences
#  of VERB, ADVERB, ADJECTIVE, and NOUN. The program then prints the new madlib to the screen
#  saves the new madlib to a file if the user also provides a name for the new file. 

import os, sys
	

#addLib function takes file as arg, calls replacePromt for each line and returns list of
#updated lines
def addLib(tfile):
	outlist = []
	#For each line in file, iterate through words and replace keywords with user input 
	for line in tfile:
		nLine = ''
		for word in line.split():
			if word == 'VERB':
				print("Enter a verb:")
				word = input()
			elif word == 'ADVERB':
				print("Enter an adverb:")
				word = input()
			elif word == 'ADJECTIVE':
				print("Enter an adjective:")
				word = input()
			elif word == 'NOUN':
				print("Enter a noun:")
				word = input()
			nLine += ' '+ word
		nLine += '\n'
		outlist.append(nLine)

	return outlist

tFile = open('./'+str(sys.argv[1]),'r')
newList = addLib(tFile)
tFile.close()
for line in newList:
	print(line, end='')

