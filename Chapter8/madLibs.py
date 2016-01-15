#! python3
#  madlibs.py reads in a text file and asks the user to replace all occurences
#  of VERB, ADVERB, ADJECTIVE, and NOUN. The program then prints the new madlib to the screen,
#  and saves the new madlib to a file if the user also provides a name for the new file. 

import os, sys, re

#Global Regex to match any keyword, can handle punctuation
addWord = re.compile(r'(VERB|ADVERB|ADJECTIVE|NOUN)([,.!?]){0,1}')


#addLib function takes file as arg, calls replacePromt for each line and returns list of
#updated lines
def addLib(tfile):
	outlist = []
	#For each line in file, iterate through words and replace keywords with user input 
	for line in tfile:
		nLine = ''
		for word in line.split():
			wMatch = addWord.search(word)
			if wMatch:
				if wMatch.group(1) == 'VERB':
					print("Enter a verb:")
					word = input()
				elif wMatch.group(1) == 'ADVERB':
					print("Enter an adverb:")
					word = input()
				elif wMatch.group(1) == 'ADJECTIVE':
					print("Enter an adjective:")
					word = input()
				elif wMatch.group(1) == 'NOUN':
					print("Enter a noun:")
					word = input()
				
				if	wMatch.group(2): 
					nLine += ' '+word+(wMatch.group(2))

				else:
					nLine += ' '+word
			
			else: 
				nLine += ' '+ word
		nLine += '\n'
		outlist.append(nLine)

	return outlist

tFile = open('./'+str(sys.argv[1]),'r')
newList = addLib(tFile)
tFile.close()
for line in newList:
	print(line, end='')
if len(sys.argv) == 3:
	outfile = open('./'+sys.argv[2], 'w')
	for line in newList:
		outfile.write(line)
	outfile.close()
