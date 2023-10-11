'''
Julissa Paramo
10 / 10 / 23
Car Wash
'''
# matching input with keys in a dictionary 
# for loops in dictionaries

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }

service_choice1 = input()

service_choice2 = input()

print('ZyCar Wash\nBase car wash - $10')

sum1 = 0

for choice in services.keys():

    if choice == service_choice1:

        sum1 = sum1 + services[choice]

        print(f'{service_choice1} - ${(services[choice])}')

sum2 = 0

for choice in services.keys():

    if choice == service_choice2:

        sum2 = sum2 + services[choice]

        print(f'{service_choice2} - ${(services[choice])}')


print(f'-----\nTotal price: ${10 + sum1 + sum2}')
