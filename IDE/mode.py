'''
Julissa Param0
10 / 9 / 23
Finding the Mode
'''
# lists
# dicitonaries
# making dictionaries out of lists


'''
data = [3,3,2,2,2,2,4,4,4,14,14]
data = [
		10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
	]

data = [1,2,2,2,3,3,4,4,4,5]
'''


# Creating Dictionary for frequency of each number in a list

numdict = {} # empty to begin with - - - {1:1, 2:3, 3:2, 4:3, 5:1}

for num in data: # iterates through each element in the list
    
    if num in numdict: # checks if the number is in the dictionary
           
        numdict[num] = numdict[num] + 1 # if it finds the key again, adds one to the value after it appears again in data
                
    else:
        
        numdict[num] = 1 # assigns 1 as the value for the number if its not in the dict
        

# Finding the Mode
        
max_value = None # no values yet for the mode

max_key = None

for key, value in numdict.items(): # goes through items in the dictionary 
    
    if max_value is None or value > max_value: # if the value > the previously assigned value --- a new value will be assigned to the max
        
        max_value = value # to begin the first condition is T , value and key will be assigned accordingly
        
        max_key = key
        
        
# Checking for a second Mode

status = True # boolean

for key, value in numdict.items(): # this second for loop will check for duplicate values
    
	if key != max_key and value == max_value: # if the keys differ, and the values are the same, there's more than one mode
          
          print(max_key, key) # prints the two modes
          
          status = False # if it finds different keys with equal value , statement changes to False
              
if status == True: # if status is unchanged, there's only one mode
            
            print(max_key) # prints the key that has the highest value ( frequency in the list from the dictionary )

#
#
#
#
