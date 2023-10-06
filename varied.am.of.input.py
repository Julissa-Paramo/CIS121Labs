'''
Julissa Paramo
10/6/23
Varies amount of input data
'''

# takes input
# converting string to float
# for loops
# max , average

nums = (input()) # takes in input

list1 = nums.split() # turns input into a list - still a list of strings

list2 = list(map(float, list1)) # makes a new list , converts strings into floats

sortednums = sorted(list2) # creates a new sorted list

sum = 0 # starting sum for calculating the avg

for num in list2: # for loop goes through the list of floats

    sum = sum + num # running sum

avg = sum / len(list2) # calculates avg: sum / length of the list

print(f'{sortednums[-1]:.2f} {avg:.2f}') # prints the max number, and the average
