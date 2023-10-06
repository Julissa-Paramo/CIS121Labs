'''
Julissa Paramo
10/6/23
Finding the Mean and Median in a list
'''

# list arithmetic
# for loops
# if , else statements
# length of a list
# printing floats


#data_set = [3,2,1,4,5]
#data_set = [
		10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
	]
#data_set = []


# MEAN CALCULATION

if len ( data_set ) > 0: # tests if there is any data in the list

	sum = 0 # counter for fiding sum of list
	
	for num in data_set: # goes through each number in the list
	
		sum = sum + num # adds all numbers together
	
	if ( sum / len ( data_set ) ) % 1  == 0: # divides sum by how many numbers are in the list, and if the mean has no remainder

		mean = f'{sum / len(data_set):.0f}' # it will drop the remainder and this will be the mean

	else: 

		mean = f'{sum / len(data_set):.4f}' # otherwise the mean will have 4 decimals




	data_set_sorted = sorted(data_set) # creates a new list that is sorted to find the median

  

  # MEDIAN CALCULATION

	if len(data_set) % 2 == 0: # this tests if the length of list is even
    
		median = ( ( data_set_sorted [ len ( data_set ) / 2 ] ) + ( data_set_sorted [ len ( data_set ) / 2 + 1 ] ) ) / 2 # divides the length in half to find the two middle numbers, adds them together, divides by two

	else:

		median = data_set_sorted[ len(data_set) // 2] # if the length is odd, the median is the number in the middle position

	print(f'Mean = {mean}, Median = {median}') # prints the final statement

else:
	
	print('No data in list') # if there's no data in the list, there's an error








