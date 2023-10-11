'''
Julissa Paramo
10 / 10 / 23
Car Wash
'''
# matching input with keys in a dictionary 
# for loops in dictionaries

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 } # dictionary for services and their cost

service_choice1 = input() # first service 

service_choice2 = input() # second service

print('ZyCar Wash\nBase car wash - $10') # first two printed statements

sum1 = 0 # cost of first service

for choice in services.keys(): # iterates through the keys in the dictionaries

    if choice == service_choice1: # if the key name matches the service from the input then . . .

        sum1 = sum1 + services[choice] # adds the value from the key in the dictionary to the sum

        print(f'{service_choice1} - ${(services[choice])}') # prints the service and its total

sum2 = 0 # cost of second service

for choice in services.keys(): 

    if choice == service_choice2:

        sum2 = sum2 + services[choice]

        print(f'{service_choice2} - ${(services[choice])}')


print(f'-----\nTotal price: ${10 + sum1 + sum2}') # adds the price of the Base car wash from line 15 to the two service costs from the for loops
                                                    # inserts dashes above statement for organization
