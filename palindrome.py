'''
Julissa Paramo
9/30/23
palindrome
'''

word = input()

word1 = word.split()

word2 = ''.join(word1)


backward = word2[-1:0:-1] + word[0]

print(backward)


if backward == word2:
    print(f'palindrome: {word}')

else:
    print(f'not a palindrome: {word}')
