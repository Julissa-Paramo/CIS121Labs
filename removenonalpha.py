'''
Julissa Paramo
9/30/23
nonalpha
'''
#removes all characters that aren't letters

word = input()

for letter in word:

    num = ord(letter) # retreieves the ASCII value of each character in the string

    if 65 <= num <= 90 or 97<= num <= 122: # intervals for a-z and A-z

        let = chr(num) # converts value back to character
        
        print(f'{let}', end='') # prints characters consecutively
        
print()
        
