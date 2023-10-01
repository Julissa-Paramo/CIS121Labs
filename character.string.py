'''
Julissa Paramo
9/30/23
how many characters in a phrase?
'''

phrase = input() #enter a character followed by a phrase 'n chicken nuggets'

phrase.split() # splits the phrase into tokens


letter = phrase[0] # assigns the first token to letter variable ( the character )

new_phrase = phrase[1:] # creates a new phrase excluding the first token

amount = new_phrase.count(letter) # counts how many characters are in the new phrase

if amount == 1:

    print(f"{amount} {letter}")

else:

    print(f"{amount} {letter}'s")

