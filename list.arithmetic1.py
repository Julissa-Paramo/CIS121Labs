'''
Julissa Paramo
10/6/23
Making a new list from another list
'''
#makes a new (list4) that consists of elements from lists 1,2, and 3


#list1, list2, list3 = [1,2,3], [4,5,6], [7,8,9]
#list1, list2, list3 = [5,-2,4], [3,12,9], [8,4,-6]
#list1, list2, list3 = [], [], []
#list1, list2, list3 = [7,3,5,7,1], [2,2,3,-3,4], [5,6,5,4,5]
#list1, list2, list3 = [4,4], [3,2], [8,9,1]
#list1, list2, list3 = [6.3,8.4,9.2], [-1.2,7.6,3.2], [4.1,-2.1,9.6]


list4 = [] # empty list to begin with

if len(list1) == len(list2) == len(list3): # checks if all three lists are the same length
       
	for num in range (len(list1)) : # goes through each index in the list

		list4.append(list1[num] * list2[num] - list3[num]) # each calculation made for each idex is appendeded to list 4

	print(list4) # prints the new list

else:
									
	print('All lists are required to be the same length.') # if they're not the same length there's an error
