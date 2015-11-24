def list2String(lst):
	x = ''
	for i in range(len(lst)):
		if i == len(lst) - 1:
			x = x+'and ' + lst[i]
		else:
			x = x + lst[i] + ', '
	print(x)

spam = ['apples', 'bananas', 'tofu', 'cats']
list2String(spam)
spam = ['test']

list2String(spam)
