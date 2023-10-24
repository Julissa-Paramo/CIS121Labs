'''
Julissa Paramo
10 / 23 / 22
'''
# functions
# for loops
# calling functions inside other functions


def factorial(n): # function name and parameters

	factorial = 1 # factorial starts off as 1 ( multiplied to anything )

	for num in range(n, 1,-1): # range starts at the number and decrements by 1 each time

		factorial = factorial * num # value of factorial changes every iteration as each number is multipled by 1 less than that number

	return factorial

def combination(m,k):
	
	return (factorial(m)) / (factorial(k) * factorial(m-k)) # uses above function to create a new formula
