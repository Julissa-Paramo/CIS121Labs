'''
Julissa Paramo
9/30/23
how many charaters in a phrase?
'''

phrase = input() 

phrase.split()


letter = phrase[0]

new_phrase = phrase[1:]

amount = new_phrase.count(letter)

if amount == 1:

    print(f"{amount} {letter}")

else:

    print(f"{amount} {letter}'s")

