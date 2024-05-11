"""
spin_on_beeper.py

Karel walks a row, spinning whenever it lands on a beeper.

Programmer: Surajit A. Bose, Date: May 3, 2024
"""

from karel.stanfordkarel import *

def main():  
    """
    Walk the length of a row, spinning when on a beeper.
    
    Preconditions: Karel is facing east at the beginning of a row.
        There are beepers at various corners in the row.
    
    Postconditions: Karel is at the end of the row, facing east.
        Karel has spun 360º wherever there is a beeper.
    """
    if beepers_present():    #  Fencepost problem: there could be a beeper at [1,1]
        spin()
    while front_is_clear():
        move()
        if beepers_present():
            spin()

def spin():
    """
    Make Karel turn 360º.
    
    Preconditions: None.
    
    Postconditions: Karel has executed a 360º spin.
    """
    for i in range(4):
        turn_left()

# don't change this code
if __name__ == '__main__':
    main()
