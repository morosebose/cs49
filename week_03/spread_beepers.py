"""
spread_beepers.py

Karel needs to spread out a pile of beepers to cover as many consecutive corners 
as there are beepers. 
Note: (1) Karel does not know how to count 
    (2) Karel's bag has infinite beepers
    (3) The row is long enough to accommodate all beepers in its pile
    (4) A beeper will never need to be placed in the last column of a row.
        
Programmer: Surajit A. Bose, Date: 2024.04.26
"""

from karel.stanfordkarel import *

def main():
    """
    Spread beepers for a single row.
    
    Preconditions: Karel is standing at the end of a row facing east.
        Somewhere in the row is a pile of n beepers.
        
    Postconditions: Beepers are spread out over n corners. 
        Karel is back to the original position.
    """
    move_to_pile()
    spread_beepers()
    
def move_to_pile():
    """
    Move Karel to the beeper pile.
    
    Preconditions: Karel is facing east at the beginning of a row.
    
    Postconditions: Karel is atop the pile of beepers.
    """
    while no_beepers_present():
        move()

def spread_beepers():
    """
    Pick up each beeper and place it where required.
    
    Preconditions: There are one or more beepers in the pile.
    
    Postconditions: Beepers are spread out over consecutive corners, 
    beginning with the corner that had the pile. 
    """ 
    while beepers_present():
        pick_beeper()
        if beepers_present():  # it's not the last beeper
            place_current_beeper()
            return_to_pile() 
        else:                  # last beeper in pile
            put_beeper()
            return_home()
            
def place_current_beeper():
    """
    Move to where beeper needs to be, and place it.
    
    Preconditions: Karel has picked one beeper from pile.
    
    Postconditions: The beeper is where it should be.
    """
    while beepers_present():
        move()
    put_beeper()
            
def return_to_pile():
    """
    Move Karel back to the pile of beepers.
    
    Preconditions: Karel has put down a beeper.
    
    Postconditions: Karel is back on the pile for the next beeper.
    """ 
    return_home()    
    move_to_pile()

def return_home():
    """
    Bring Karel back to initial position.
    
    Preconditions: Karel is somewhere in the row, facing east.
    
    Postconditions: Karel is at the first corner, facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    """
    Karel does a 360º.
    
    Preconditions: Karel faces one direction.
    
    Postconditions: Karel faces the opposite direction.
    """
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()  