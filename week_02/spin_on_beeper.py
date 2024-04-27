from karel.stanfordkarel import *
"""
Karel walks a row, spinning whenever it lands on a beeper.
Pre: Karel is facing east at the beginning of a row.
Post: Karel is at the end of the row, facing east.
"""
def main():  
    """Walk to the end of the row, spin when on a beeper."""
    if beepers_present():		#  Fencepost problem: there 
        spin()					#  could be a beeper at [1,1]         
    while front_is_clear():
        move()
        if beepers_present():
            spin()

def spin():
    """Turn 360º."""
    for i in range(4):
        turn_left()

# don't change this code
if __name__ == '__main__':
    main()