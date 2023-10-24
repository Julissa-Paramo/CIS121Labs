'''
Julissa Paramo
10 / 23 / 23 
'''
# function for finding the LCM
# for loops
# break statements
# if statements
# and booleans

def LCM(int_1,int_2): # function name and parameters

	for num in range ( 1, int_1 * int_2 + 1 ): # for loop will go through all numbers from 1 to the max LCM possible

		if num % int(int_1) == 0 and num % int(int_2) == 0: # if the number is a multiple of both integers

			break # loop ends if conditions are met 

	return num # returns the LCM
