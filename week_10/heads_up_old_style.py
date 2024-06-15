"""
heads_up_old_style.py

Console version of heads up

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
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line:
            lines.append(line)
    f.close()
    return lines


def main():
    words = get_words_from_file()
    while True:
        word = random.choice(words)
        input(f'{word} ')
    

if __name__ == '__main__':
    main()