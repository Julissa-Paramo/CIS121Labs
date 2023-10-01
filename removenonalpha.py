'''
Julissa Paramo
9/30/23
nonalpha
'''

word = input()

for letter in word:

    num = ord(letter)

    if 65 <= num <= 90 or 97<= num <= 122:

        let = chr(num)
        
        print(f'{let}', end='')
        
print()
        
