input_month = input()
input_day = int(input())

if input_month =='March':
    if 20 <= input_day <= 31:
        print('Spring')
elif input_month =='April':
    if 1 <= input_day <= 30:
        print('Spring')
elif input_month =='May':
    if 1 <= input_day <= 31:
        print('Spring')
elif input_month =='June':
    
    if 1 <= input_day <= 20:
        print('Spring')
        
elif input_month =='June':
    if 21 <= input_day <= 30:
        print('Spring')
        
elif input_month =='July':
    if 1 <= input_day <= 31:
        print('Summer')
elif input_month =='August':
    if 1 <= input_day <= 31:
        print('Summer')
elif input_month =='September':
    if 1 <= input_day <= 21:
        print('Summer')
        
        
elif input_month =='September':
    if 22<= input_day <= 30:
        print('Autumn')
elif input_month =='October':
    if 1<= input_day <= 31:
        print('Autumn')
elif input_month =='November':
    if 1<= input_day <= 30:
        print('Autumn')
elif input_month =='December':
    if 1<= input_day <= 20:
        print('Autumn')
        
        
elif input_month =='December':
    if 21<= input_day <= 31:
        print('Winter')
elif input_month =='January':
    if 1<= input_day <= 31:
        print('Winter')
elif input_month =='February':
    if 1<= input_day <= 29:
        print('Winter')
elif input_month =='March':
    if 1<= input_day <= 19:
        print('Winter')
else:
    print('Invalid')

