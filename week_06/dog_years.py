"""
dog_years.py

Ask the user to enter an age in human years. Using the equation 1 human year = 7 dog years. convert the entered age into dog years. 
- If the user enters a negative number, ask the user to try again
- Continue asking for another age in human years until user enters 0 to stop.

Programmer: Surajit A. Bose, Date: 2024.05.17
"""

# Constants
DOG_YEAR_MULTIPLIER = 7
SENTINEL = 0

def main():
    """
    Get a series of human ages from user input. Print the respective dog ages to screen.
    
    Preconditions: None
    
    Postconditions: 
    - User input is checked
    - When appropriate, the age in dog years is displayed on the console.
    """
    
    age = int(input("Enter an age in human years: "))
    while age != SENTINEL :
        if age < 0 :
            print(f"Sorry, please enter a positive number or {SENTINEL} to exit")
        else :
            print(f"The age in dog years is {age * DOG_YEAR_MULTIPLIER}")
        age = int(input("Enter an age in human years: "))


if __name__ == '__main__':
    main()