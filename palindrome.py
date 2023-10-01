'''
Julissa Paramo
9/30/23
palindrome
'''
#checks if the input is a palindrome
#reversing string
#splitting and joining

word = input() 

word1 = word.split() # splits words into tokens if there are any

word2 = ''.join(word1) # joins any existing tokens together so the string can be read without spaces

backward = word2[-1:0:-1] + word[0] # reverses the order of the string

if backward == word2:
    print(f'palindrome: {word}') # if the reversed order matches the original order, prints palindrome

else:
    print(f'not a palindrome: {word}')
