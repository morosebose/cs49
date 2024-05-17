"""
rochambeau.py

Play five rounds of a text-based rock, paper, scissors game. 

Programmer: Surajit A. Bose, Date: 2024.05.17
"""

import random

NUM_ROUNDS = 5

def main():
    """
    Play specified number of rounds of rochambeau / rock, paper, scissors.
    
    Preconditions: 
    - Rock is defined as 1, Paper as 2, Scissors as 3
    - Agreed-upon rules: Rock crushes scissors, Scissors cuts paper, Paper covers rock
    
    Postconditions:
    - Game is played specified number of times and scored correctly
    - The number of times the human user wins is displayed to screen
    """    
    player_won = 0

    for i in range(NUM_ROUNDS):
        computer = random.randint(1, 3)
        player = int(input('Your move(1, 2, or 3): '))
        if computer == player :
            print("It's a tie!")
        elif player == 1 :
            if computer == 2:
                print('You Lose! Paper covers rock')
            else:
                print('You Win! Rock crushes scissors')
                player_won += 1
        elif player == 2 :
            if computer == 1 :
                print('You Win! Paper covers rock')
                player_won += 1
            else:
                print('You Lose! Scissors cuts paper')
        else:
            if computer == 1: 
                print('You Lose! Rock crushes scissors')
            else: 
                print('You win! Scissors cuts paper')
                player_won += 1
    print(f'You won {player_won} rounds!')


if __name__ == '__main__':
    main()