'''
Julissa Paramo
10 / 6 / 23
Filter and Sort a List
'''
# returns only the negative values from largest to smallest from an input
# list to string print statements
# for loops in lists

nums = input() # numbers are inputted

nums1 = nums.split() # creates a list of strings from the numbers 

nums2 = list(map(int, nums1)) # makes a new list of integers

sortedlist = sorted(nums2) # sorts the list from smallest to largest integrers

negvals = [] # empty list

for num in sortedlist: # iterate through each integer in the list

    if num < 0: # checks if the integer is negative

        negvals.append(num) # adds the integer to the empty list
        
print(' '.join(map(str, negvals[::-1]))) # negvals[::-1] returns the list in reverse order
                                        # list is converted to a string with (map(str, x)
                                        # list is concatenated by ' ' with join function
