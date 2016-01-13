#! python3
#  randomQUizGenerator.py - Creates quizes with questions and answers in random order,
#  along with the same key.

import random

# The quiz data. Keys are states and values are the capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
		'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
		'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
		'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
		'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
		'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
		'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
		'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
		'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
		'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
		Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
		'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
		'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
		'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
		'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
		'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
		Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate quiz files.
for quizNum in range(10):
	#todo: create the quiz and answer key fies.
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

	#todo: write out the header for the quiz
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20 ) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))

	
	#todo: shuffle the order of the states
	states = list(capitals.keys())
	random.shuffle(states)

	#todo: loop through all 50 states, making a question for each
	for questionNum in range(50):
		#Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		#todo: write the questions and answer options to the quiz file.
		quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
		
		for i in range(4):
			quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		#todo: write the answer key to a file.
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 
			'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()



