#!/usr/bin/python3.5
#bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of 
#text on the clipboard

import pyperclip

#Obtain clipboard text
text = pyperclip.paste()

#Spearate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):        #loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i] #add a star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
