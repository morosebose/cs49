"""
fruit_list.py

Practice using list indices

Programmer: CS 49 instruction team, Date: 2024.06.14
"""

import random

def main():
    # 1. Understand how to create a list and add values
    # A list is an ordered collection of values
    names = ['Julie', 'Mehran', 'Simba', 'Ayesha']
    names.append('Karel')

    # 2. Understand how to loop over a list
    # this prints the list to the screen one value at a time
    for value in names:
        print(value)

    # 3. Understand how to look up the length of a list
    # use randint to select a valid "index" 
    max_index = len(names) - 1
    ind = random.randint(len(names) * -1, max_index)

    # 4. Understand how to get a value by its index
    # get the item at the chosen index
    correct_answer = names[ind]

    # prompt the user for an answer, check if it is correct
    prompt = f'Who is at index... {ind}? '
    answer = input(prompt)
    if answer == correct_answer:
        print('Good job')
    else:
        print(f'Correct answer was {correct_answer}')

if __name__ == '__main__':
    main()