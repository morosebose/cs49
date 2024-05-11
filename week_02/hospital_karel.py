"""
hospital_karel.py

Karel begins at the left end of a row that has beepers at various points.
The beepers indicate spots where a hospital should be built.
Hospitals are two adjacent columns of three beepers each.

Programmer: Surajit A. Bose, Date: 2024.04.26
"""

from karel.stanfordkarel import *

def main():
    """
    Walk the row and build hospitals where indicated.
    
    Preconditions: Karel is at one end of the row, facing east.
        Beepers on the row indicate future hospital locations.
        
    Postconditions: Hospitals built.
        Karen is at the other end of the row, facing east.
    """
    while front_is_clear():
        move_to_supplies()
        build_hospital()
        if front_is_clear():
            move()
            
def move_to_supplies():
    """
    Move Karel to location of hospital.
    
    Preconditions: Karel is on a corner with no supplies (beeper), facing east
    
    Postcondition: Karel has moved to a corner with a beeper and picked the beeper.
        Karel is facing east.
    """
    while no_beepers_present():
        move()
    pick_beeper()

def build_hospital():
    """
    Build hospital at current corner.
    
    Preconditions: Karel is on a corner where a hospital is to be built.
        Karel is facing east.
    
    Postconditions: Karel is on the west corner of the built hospital, facing east.
    """
    turn_left()
    build_column()
    turn_right()
    move()
    turn_right()
    build_column()
    turn_left()

def build_column():
    """
    Build a single column of beepers.
    
    Preconditions: Karel is correctly oriented to place three consecutive beepers.
    
    Postconditions: Karel has placed the three beepers. 
    """
    for i in range(2):
        put_beeper()
        move()
    put_beeper()

def turn_right():
    """
    Turn Karel to its right.
    
    Preconditions: None.
    
    Postconditions: Karel is facing to its right from its original direction. 
    """
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()