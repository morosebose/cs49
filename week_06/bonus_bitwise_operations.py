"""
bonus_bitwise_operations.py

Demonstrate the operations of bitwise & and |. 

Programmer: Surajit A. Bose, Date: 2024.05.20
"""

def bitwise_operations():
    a = 3        # decimal 3: binary 011
    b = 6        # decimal 6: binary 110
    c = 3 & 6    # result: binary 010, or decimal 2
    d = 3 | 6    # result: binary 111, or decimal 7

    print(f'Result of bitwise and, 3 & 6 : {c}')
    print(f'Result of bitwise or,  3 | 6 : {d}')

if __name__ == '__main__':
    bitwise_operations()