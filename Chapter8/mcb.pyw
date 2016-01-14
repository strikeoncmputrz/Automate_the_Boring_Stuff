#! python3
#  mcb.pyw - Saves and loads pieces of text to the clipboard.
#  Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
#	  python mcb.pyw <keyword> - Loads clipboard to keyword.
#	  python mcb.pyw list - Loads all keywords to clipboard.
#	  python mcb.pyw delete <keyword> - Deletes a saved <keyboard> clipboard. 
#	  python mcb.pyw delete-all - Deletes all saved clipboards.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()

#Delete saved clipboard associated with key <keyword>
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	if sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
	#List keywords, delete all keywords, or load content if <keyword> matches.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1].lower() == 'delete-all':
		for key in mcbShelf:
			del mcbShelf[key]
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
