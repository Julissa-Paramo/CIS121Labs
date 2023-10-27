'''
Julissa Paramo
10 / 24 / 23
'''
#TODO:Import math module

import math

def quadratic_formula(a, b, c):
    x1 = ( -b + ( math.sqrt (b**2 - 4*a*c) ) ) / (2*a)
    x2 = ( -b - ( math.sqrt (b**2 - 4*a*c) ) ) / (2*a)
    return (x1, x2)
    

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print(f'{prefix_str}{number:.0f}')
    else:
        print(f'{prefix_str}{number:.2f}')
    

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
    print_number(solution[0], 'x1 = ')
    print_number(solution[1], 'x2 = ')
