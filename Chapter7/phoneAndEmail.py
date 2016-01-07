#! /usr/bin/python3
#phoneAndEmail.py finds all of the phone numbers and email addresses in 
#the currently copied clipboard text and pastes them to the clipboard

import pyperclip, re

#Regex for finding phone numbers. Area code and extension (2-5 digits) are optional
phoneRegex = re.compile(r'''(
		(\d{3}|\(\d{3}\))?	#area code
		(\s|-|\.)?		#separator
		(\d{3})			#first three digits
		(\s|-|\.)?		#separator
		(\d{4})			#last four digits
		(\s*(ext|x|ext\.)\s*(\d{2,5}))? #extension
		)''', re.VERBOSE)


#Create book's email regex
emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+	#username	***would not run with ._+-%
		@			#@ symbole
		[a-zA-Z0-9.-]+		#domain name
		(\.[a-zA-Z]{2,4})	#dot something 
		)''', re.VERBOSE)

#Find all matches in the clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#Copy the results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')



	
