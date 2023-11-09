'''
Julissa Paramo
11 / 6 / 23
Fruit Data
'''
from Julissa_Paramo_Stats import Mean,Median # imports the Mean and Median functions from Julissa_Paramo_Stats module

apple_am = [] # list of amount_eaten

banana_am = []

strawberry_am =[]

total_data = []


with open('500DayFruitData.txt','r') as file: # opening the file to read

    lines = file.readlines()[1:] # lines variable are the lines as lists in the file , begins reading at line 1 ; line 0 is not data

    for i in lines: # for loop will iterate through each line list from top to bottom

        date, type, amount_eaten = i.strip().split() # sets split data with the following variables, strips the whitespace + splits data

        total_data.append(int(amount_eaten)) # adds amount_eaten to list used to calculate Mean and Median for the fruit

        if type == 'apple': # adding to apple data 

            apple_am.append(int(amount_eaten)) # txt file is string with open 'r', uses data as int to calculate stats

        if type == 'banana': # adding to banana data

            banana_am.append(int(amount_eaten))

        if type == 'strawberry': # adding to strawberry data

            strawberry_am.append(int(amount_eaten))


with open('Julissa_Paramo_Output.txt','w') as txtfile:

    txtfile.write('The mean number of apples eaten is {:.2f} \n'.format(Mean(apple_am))) # calls function to find the Mean and Medians of a list of nums
    txtfile.write('The median number of apples eaten is {:.2f} \n'.format(Median(apple_am)))

    txtfile.write('The mean number of bananas eaten is {:.2f} \n'.format(Mean(banana_am)))
    txtfile.write('The median number of bananas eaten is {:.2f} \n'.format(Median(banana_am)))

    txtfile.write('The mean number of strawberries eaten is {:.2f} \n'.format(Mean(strawberry_am)))
    txtfile.write('The median number of strawberries eaten is {:.2f} \n'.format(Median(strawberry_am)))

    txtfile.write('The mean number of all fruit eaten is {:.2f} \n'.format(Mean(total_data)))
    txtfile.write('The median number of all fruit eaten is {:.2f}'.format(Median(total_data)))

