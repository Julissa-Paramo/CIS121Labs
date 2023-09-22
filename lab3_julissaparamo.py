"""
Julissa Paramo
9/7/23
Lab 3 Selection Statements
"""

earned_income = float ( input ( 'Enter the amount of income you earned in 2023: ' ) )
marital_status = input ( 'Are you married or single?\nType m for married and s for single: ' )


if marital_status == 's':
    
    if 0 <= earned_income <= 11000:
        print ( 'This year you owe ' f'{ earned_income * .1 :.2f}' ' in taxes' )

    elif 11001 <= earned_income <= 44725:
        print ( 'This year you owe ' f'{ ( earned_income - 11000 ) * .12 + 1100:.2f}' ' in taxes' )

    elif 44276 <= earned_income <= 95375:
        print ( 'This year you owe ' f'{ ( earned_income - 44725 ) * .22 + 1100 + ( 44725 - 11000 ) *.12 :.2f}' ' in taxes' )

    elif earned_income > 95375:
        print ( 'You made too much for this calculator. Hurray!' )

elif marital_status == 'm':

    if 0 <= earned_income <= 22000:
        print ( 'This year you owe ' f'{ earned_income * .1 :.2f}' ' in taxes' )

    elif 22001 <= earned_income <= 89450:
        print ( 'This year you owe ' f'{ ( earned_income - 22000 ) * .12 + 2200 :.2f}' ' in taxes' )

    elif 89451 <= earned_income <= 190750:
        print ( 'This year you owe ' f'{ ( earned_income - 89450 ) * .22 + 2200 + ( 89450 - 22000 ) * .12 :.2f}' ' in taxes' )

    elif earned_income > 190750:
        print ( 'You made too much for this calculator. Hurray!' )
    

