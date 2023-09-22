'''
Julissa Paramo
9/22/23
Prime Numbers
'''

num = 2
count = 2

for i in range( 2 , 251 ) :

    status = True

    for j in range ( 2 , i ):

        if i % j == 0 :

            status = False

    if status == True :
            
            print ( i )
            