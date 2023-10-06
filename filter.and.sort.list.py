'''
Julissa Paramo
10 / 6 / 23
Filter and Sort a List
'''
# returns only the negative values from largest to smallest from an input
# list to string print statements
# for loops in lists

nums = input() # numbers are inputted

nums1 = nums.split() # numbers are split into tokens

negvals = [] # empty list for the negative values


for num in nums1: # iterates through elements
    
    if int(num) < 0: # int(num) converts the element from a string to an integer + checks if it's negative
        
        negvals.append(int(num)) # adds negative integer to the empty list
        

negvals.sort(reverse=True) # sorts from smallest to largest , then reverses the order


for num in negvals: # creates a copy of the reversed list and prints the elements with a space in between
    
    print(num, end=' ')
