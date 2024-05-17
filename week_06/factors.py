"""
factors.py

Ask the user to enter a positive integer. Print all its factors to screen. 
Repeat with new integer until user wants to stop.

Programmer: Surajit A. Bose, Date: 2024.05.17
"""


SENTINEL = 0

def main():
    """
    Get and check user input. If input is a positive integer, print factors to screen.
    
    Preconditions: None
    
    Postconditions:
    - User input is checked
    - Where appropriate, factors are printed to screen.
    """
    
    num = int(input('Your number: '))
    while num != SENTINEL :
        if num < 0 :
            print('Please input a positive number')
        else:
            for i in range(1, num + 1) :
                if (num % i) == 0 :
                    print(i)
        num = int(input('Your number: '))
    


if __name__ == '__main__':
    main()