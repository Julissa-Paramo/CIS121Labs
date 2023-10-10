'''
Julissa Paramo
9 / 21 / 23
8 x 10 Multiplication Table
'''

#muliplication table for 8 x 10
#nested for loops
#spacing details

for i in range ( 1 , 9 ) :
    
    for j in range ( 1 , 11 ) :

        if i * j // 10 == 0 :

            print ( '' , i * j , end=' ' )

        else:

            print ( i * j , end=' ' )

    print ( )
