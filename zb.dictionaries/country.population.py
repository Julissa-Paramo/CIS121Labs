'''
Julissa Paramo
Country Population
10 / 10 / 23 
'''

user_input = input() # sample input "China:1365830,India:124720,United States:3184,Indonesia:12734"


entries = user_input.split(',') # splits the input at each comma, making a list
                  
                                # ['China:1365830', 'India:124720', 'United States:3184', 'Indonesia:12734']
country_pop = {} # empty dictionary


for pair in entries: # going through each element in the list 'entries' --- one element = 'China:1365830' & 'India:124720' ect.


    split_pair = pair.split(':') # creates a new list called split_pair that splits the element at ':'


    country_pop[split_pair[0]] = split_pair[1] # {'China': '1365830'}
 

    country = split_pair[0]


    pop = split_pair[1]

    
    print(f'{country} has {pop} people.')
