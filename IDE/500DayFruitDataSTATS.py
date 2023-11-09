'''
Julissa Paramo
11 / 6 / 23
Fruit Data Lab
'''


def Mean(listA):  # takes numbers in a list to find the average

    sum = 0 # sum starts at 0

    for num in listA: # for loop to iterate through the list

        sum += num # addd each num to sum

    return sum / len(listA) # sum divided by len(list) which is total elements in a list 


def Median(listA): # takes numbers in a list to find the median

    if len(listA) % 2 == 0: # if the amount of eleemetns is even . . .

        num1 = sorted(listA)[(len(listA)//2)] # first num 

        num2 = sorted(listA)[(len(listA)//2-1)] # second num is the number behind it ( num 1 and num 2 are the two middle nums )

        return (num1+num2) / 2 # returns average of the two middle nums to find the real median
    
    else: # amount of elements in list is odd 

        return sorted(listA)[len(listA)//2] # sorts list and finds middle index through int division
    
