'''
Julissa Paramo
10 / 9 / 23
Lab 7 - Dictionaries
'''

# dictionaries
# boolean statements

phone_book = {} # empty dictionary to add to 


print("When entering a name and number, please enter names with underscores.\n" +
      "For example: Matt_Priem, 507-389-1438. When done, type 'quit'\n") # user instructions

while True: # boolean value

	name_num = input("Name and number: ") # get input from user 


	if name_num == 'quit': # if user types quit . . .

		break # loop ends and the input question will not print


	else: # if the input is not 'quit'

		listOfNums=name_num.split() # this will split the user input at ' ' and make a list containing 
										# two elements ; a name and a number
		phone_book[listOfNums[0]]=listOfNums[1] # this adds the two elements to the dictionary
												# the first index [0] (key) = index [0] (value)

print(phone_book) # prints the dictionary
