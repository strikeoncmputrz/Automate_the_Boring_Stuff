#!/usr/bin/python3
#This function implements the python split() function using regex

import re

def regexSplit(*args):
	#If the only arguement is a string regex removes 
	#beginning and end whitespace characters
	if(len(args) == 1):
		frontreg = re.compile(r'^\s*')
		backreg  = re.compile(r'\s*$')
		return frontreg.sub('',backreg.sub('',args[0]))
	else:
		toRemove = re.compile(args[1])
		return toRemove.sub('',args[0])


print('The split string is:' + regexSplit('    four    ') +'.')
print('The split string is:' + regexSplit('hello yello othelo', 'elo') +'.')
print('The split string is:' + regexSplit('    exit on the gift %4545','%45') +'.')

