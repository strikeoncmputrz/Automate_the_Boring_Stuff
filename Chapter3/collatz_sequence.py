#This program asks the user to enter in a number and then returns it's Collatz sequence.


#This function returns a Colatz number given an int as a parameter
def collatz(number):
	if number % 2:
		c = (3 * number + 1)
	else:
		c = number // 2
	print(str(c))
	return c

#This asks for user input and calls Collatz
print('Enter an integer to see its Collatz sequence.')

try: 
	x = int(input())

except  ValueError:
	print('User must enter an integer. Enter integer now!')
	x = int(input())

while x != 1:
	x = collatz(x)
