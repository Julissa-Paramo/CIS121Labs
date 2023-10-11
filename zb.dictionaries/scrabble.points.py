'''
Julissa Paramo
10 / 10 / 23
Scrabble Points
'''
# gets a word from user
# dictionary holds point system for each letter in the alphabet
# for loops
# dictionary methods 

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }    # dictionary that holds integer values for each letter

phrase = input() # user inputs a word 'PYTHON"

letters = phrase.split() # creates a list from word ['P','Y','T','H','O','N']

sum = 0 # sum counter for the points

for letter in phrase: # goes through each element in the list 'letters' - - PYTHON

    sum = sum + (tile_dict.get(letter, 'n/a')) # adds the value from the dictionary whose key matches the element in 'letters'

print(f'{phrase} is worth {sum} points.') # prints how many points the word is worth

    
