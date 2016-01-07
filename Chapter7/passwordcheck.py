#!/usr/bin/python3
#Program designed to determine if a password meets strength requirements.
#A strong password is defined as one that is at least eight characters long, 
#contains both uppercase and lowercase characters, and has at least one digit.

import re

def isStrongPwd(pwd):
	
	#Define a regex for each condition
	eightChars = re.compile(r'\w{8,}')
	uppers = re.compile(r'[A-Z]')
	lowers = re.compile(r'[a-z]')
	digit = re.compile(r'\d+')
	
	#Test each condition
	if((eightChars.search(pwd) != None)
		& (uppers.search(pwd) != None)
		& (lowers.search(pwd) != None)
		& (digit.search(pwd) != None)
	):
		print(pwd + ' is a strong password.')
	else:
		print(pwd + ' is not strong enough.')


print("Type in your password to test it's strength.")
pwd = input()
isStrongPwd(pwd)
