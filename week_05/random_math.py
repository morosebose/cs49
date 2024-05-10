"""
random_math.py

Illustrate use of import statements, the math library, and the random module.
Along with companion module math_random.py, illustrate the difference between
from ... import and a bare import. 

Programmer: Surajit A. Bose
"""

# import statements
from random import randint
import math


def main():
    """
    Generate four random numbers between 200 and 1000. Calculate their square roots.
    Print each number and its square root to the screen. 
    """
    for i in range(4):
        my_num = randint(200, 1000)
        my_sqrt = math.sqrt(my_num)
        print(f'Number is: {my_num}, square root is: {my_sqrt}')

if __name__ == "__main__":
    main()
