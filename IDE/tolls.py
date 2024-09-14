'''
Julissa Paramo
10 / 16 / 23
Lab 8
Functions and List review
'''
# functions
# nested if statements

#Problem 1

def calc_toll(hour, is_morning, is_weekend): # function name and parameters
	if is_morning == True: # if the time is from 12 AM to 11:59 AM
		if is_weekend == False: # if it is a WEEK DAY
			if hour == 12 or 1 <= hour < 7:
				return f'${float(1.15)}'
			if 7 <= hour < 10:
				return f'${float(2.95)}'
			if 10 <= hour < 12:
				return f'${1.90:.2f}'	
		if is_weekend == True: # if it's the WEEKEND
			if hour == 12 or 1 <= hour < 7:
				return f'${float(1.05)}'
			if 7 <= hour < 12:
				return f'${float(2.15)}' 		
	if is_morning == False: # if the time is from 12 PM to 11:59 PM
		if is_weekend == False: # if it is a WEEK DAY
			if hour == 12 or 1 <= hour < 3:
				return f'${1.90:.2f}'			
			if 3 <= hour < 8:
				return f'${float(3.95)}'			
			if 8 <= hour < 12:
				return f'${1.40:.2f}'			
		if is_weekend == True: # if it's the WEEKEND
			if hour == 12 or 1 <= hour < 8:
				return f'${float(2.15)}'			
			if 8 <= hour < 12:
				return f'${1.10:.2f}'
