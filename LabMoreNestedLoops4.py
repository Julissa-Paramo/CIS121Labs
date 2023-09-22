'''
Julissa Paramo
9/22/23
Prime or Perfect
'''

for i in range ( 2 , 251 ) :

    status = True

    for j in range ( 2 , i ) :

        if i % j == 0 :

            status = False

    if status == True :
         
         print ( i )


for i in range ( 2 , 251 ) :

    sum = 0

    for j in range ( 1 , i ) :
         
         if i % j == 0 :
              
              sum = sum + j
          
    if status == True or sum == i:
            
            print ( i )