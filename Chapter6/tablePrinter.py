#Defines a function to print out a table from a list of lists of strings


def printTable(tData):
	
	#Obtain max length string in each string list
	colWidths = [0] * len(tData)	
	for i in range(len(tData)):
		for j in tData[i]:
			if len(j) > colWidths[i]:
				colWidths[i] = len(j)
	for x in range(len(tData[0])):
		for y in range(len(tData)):
			print(tData[y][x].rjust(colWidths[y] + 3), end = '')
		print()
			 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
	     ['Alice', 'Bob', 'Carol', 'David'],
	     ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
