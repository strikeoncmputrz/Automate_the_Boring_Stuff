#!/usr/bin/python3
#  mapIt.py reads an address from sys.argv or the clipboard and opens the address in google maps.

import pyperclip, sys, webbrowser

address = ''

if len(sys.argv) == 1:
	address = pyperclip.paste()

else: 
	address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + address)
