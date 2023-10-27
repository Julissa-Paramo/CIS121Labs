'''
Julissa Paramo
10 / 24 / 23
'''

# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    number = random.randint(1,100)
    if num < number:
        print(f'{num} is too low. Random number was {number}.')
    if num > number:
        print(f'{num} is too high. Random number was {number}.')
    if num == number:
        print(f'{num} is correct!')
    # TODO: Compare parameter num to the random number
    
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)
