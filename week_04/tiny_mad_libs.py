"""
tiny_mad_libs.py

Prompt the user for an adjective, noun, and verb in turn, 
then print full sentence to the screen

Programmer: Surajit A. Bose, Date: 2024.05.03
"""

def main():
    """
    Get words from user and append them to the end of the starter sentence.
    
    Preconditions: None
    
    Postconditions: User has supplied three words. 
        Full sentence is printed on screen with the user words at the ende.
    """
    sentence_start = 'Code in Place is fun. I learned to program and used Python to make my '
    adj = input('Please type an adjective and press enter. ')
    noun = input('Please type a noun and press enter. ')
    verb = input('Please type a verb and press enter. ')

    print(f'{sentence_start}{adj} {noun} {verb}!')


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()