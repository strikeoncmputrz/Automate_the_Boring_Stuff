import random

def getAnswer(aNum):
	if aNum == 1:
		return 'It is certain'
	
	elif aNum == 2:
		return 'It is decidedly so'
	
	elif aNum == 3:
		return 'Yes'

	elif aNum == 4:
		return 'Reply hazy try again'

	elif aNum == 5:
		return 'Ask again later'

	elif aNum == 6:
		return 'Concentrate and ask again'

	elif aNum == 7:
		return 'My reply is no'
	
	elif aNum == 8:
		return 'Outlook not so good'

	elif aNum == 9:
		return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
