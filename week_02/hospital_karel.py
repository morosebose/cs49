from karel.stanfordkarel import *

"""
hospital_karel.py

Karel begins at the left end of a row that has beepers at various points.
The beepers indicate spots where a hospital should be built.
Hospitals are two adjacent columns of three beepers each. 
"""


def main():
    """
    Walk the row and build hospitals where indicated.
    Pre: Karel is at one end of the row.
        Beepers on the row indicate future hospital locations.
    Post: Hospitals built.
        Karen is at the other end of the row.
    """
    while front_is_clear():
        move_to_supplies()
        build_hospital()
        if front_is_clear():
            move()
            
def move_to_supplies():
    """Move Karel to location of hospital."""
    while no_beepers_present():
        move()
    pick_beeper()

def build_hospital():
    """Build hospital at current corner."""
    turn_left()
    build_column()
    turn_right()
    move()
    turn_right()
    build_column()
    turn_left()

def build_column():
    """Build a single column of beepers."""
    for i in range(2):
        put_beeper()
        move()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()