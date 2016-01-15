#! python3
# regexSearch.py opens all .txt files in a directory and searches for any lines that
# match a user supplied regex. The file and line are printed to the screen.

import os, sys, re

# Open each file in a directory 
# If file has a .txt extension pass it to regexSearch function
def findTextFiles():
	
	txt = re.compile(r'.*(.txt)$') # regex for finding '.txt'
	
	onlyfiles = [f for f in os.listdir('./') if os.path.isfile(os.path.join('./', f))]
	textFiles = [f for f in onlyfiles if txt.match(f)] 

	return textFiles

# Regex Search iterates through each line in a file
# If regex is found, the function prints the line number, line, and filename
def regexSearch(fileN):
	lineN = 1
	file = open('./'+fileN, 'r')
	for line in file:
		matchedLine = reg.search(line)
		if matchedLine:
			print(matchedLine.group()+' found in "'+fileN+'" Found on line #'+str(lineN)+'. '+line)

# Obtain regex string from sys.argv[2]
searchString = sys.argv[1]
print("Searchstring = "+searchString)
reg = re.compile(searchString)

fileList = findTextFiles()
print("fileList = "+str(fileList))

for file in fileList:
	regexSearch(file)

