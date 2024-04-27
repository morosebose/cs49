from karel.stanfordkarel import *

"""
spread_beepers_multiple.py

Karel needs to spread out a pile of beepers to cover
as many consecutive corners as there are beepers. 
Note: (1) Karel does not know how to count 
    (2) Karel's bag has infinite beepers
    (3) The row is long enough to accommodate all beepers in its pile
    (4) A beeper will never need to be placed in the last column of a row.
"""
def main():
    """Spread beepers for multiple rows.
    Pre: Somewhere in each row is a pile of n beepers.
        Karel is in the bottom row first corner. 
        Karel is facing east.    
    Post: Beepers are spread over n corners in each row. 
        Karel is in the top row first corner, facing east.
    """
    spread_single_row()     # Fencepost problem
    while left_is_clear():
        move_to_next_row()
        spread_single_row() 

def spread_single_row():
    """Spread beepers for a single row.
    Pre: Karel is standing at the end of a row facing east.
        Somewhere in the row is a pile of n beepers.
    Post: Beepers are spread out over n corners. 
        Karel is back to the original position.
    """
    move_to_pile()
    spread_beepers()
    
def move_to_pile():
    """Move Karel to the beeper pile.
    Pre: Karel is facing east at the beginning of a row.
    Post: Karel is atop the pile of beepers.
    """
    while no_beepers_present():
        move()

def spread_beepers():
    """Pick up each beeper and place it where required.
    Pre: There are one or more beepers in the pile.
    Post: Beepers are spread out over consecutive
        corners, beginning with the corner that had 
        the pile. 
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
    """Move to where beeper needs to be, and place it.
    Pre: Karel has picked one beeper from pile.
    Post: The beeper is where it should be.
    """
    while beepers_present():
        move()
    put_beeper()
            
def return_to_pile():
    """Move Karel to the pile of beepers.
    Pre: Karel has put down a beeper.
    Post: Karel is back on the pile for the next beeper.
    """ 
    return_home()    
    move_to_pile()

def return_home():
    """Bring Karel back to initial position.
    Pre: Karel is somewhere in the row, facing east.
    Post: Karel is at the first corner, facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    """Karel does a 360º.
    Pre: Karel faces one direction.
    Post: Karel faces the opposite direction.
    """
    turn_left()
    turn_left()

def move_to_next_row():
    """Move up a row.
    Pre: Karel is facing east at the beginning of a row.
        There is a row above.
    Post: Karel is at the beginning of the row above. 
        Karel is facing east.
    """
    turn_left()
    move()
    turn_right()

def turn_right():
    """Turn Karel to its right.
    Pre: Karel is facing in a certain direction.
    Post: Karel is facing right of original direction.
    """
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()  