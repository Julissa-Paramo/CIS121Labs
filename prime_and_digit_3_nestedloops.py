
'''
Julissa Paramo
9/22/23
Prime and Digit 3
'''

for i in range ( 2 , 251 ) :

    status = True

    for j in range ( 2 , i ) :
        
        if i % j == 0:
            
            status = False
    
    if status == True and str ( i ) [ -1 ] == '3':
            
            print ( i )
