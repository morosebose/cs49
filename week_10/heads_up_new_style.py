"""
heads_up_new_style.py

Console version of heads up, using 'with open' for reading file

Programmer: CS 49 instruction team, Date: 2024.06.14
"""

import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines = []
    with open (FILE_NAME, 'r') as f:  
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line is not just whitespace, add it to the list 
            if line:
                lines.append(line)
    return lines


def main():
    words = get_words_from_file()
    while True:
        word = random.choice(words)
        input(f'{word} ')
    

if __name__ == '__main__':
    main()