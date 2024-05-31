"""
medical_test_simulator.py

Calculate the expected percentage of false negatives for a diagnostic test.

Programmer: Surajit A. Bose, Date: 2024.05.31
"""

import random

def simulate_tests(num_people, test_accuracy, infection_rate):
    """
    Calculate and display statistics about test accuracy.

    Params:
        num_people: int, the number of people getting the test 
        test_accuracy: float, how accurate the test is 
        infection_rate: float, the proportion of the population with the disease
    
    Preconditions: None

    Postconditions: 
        Number of true and false positives and negatives are printed onscreen

    Return: float, fraction of positive results that are inaccurate
    """
    # We need to tally four values. 
    # Choose variable names for them and initialize to zero.
    true_pos = 0  # etc.
    false_pos = 0
    false_neg = 0
    true_neg = 0

    # Loop over all individuals. 
    for i in range(num_people):  # what goes inside the parentheses?
        # Inside the loop:
        # - simulate whether the individual is infected
        # - simulate whether the test is accurate
        # Hint: The code 'is_true = random.random < 0.5' will
        # set the variable 'is_true' to True 50% of the time.
        # How could you probabilistically set these two variables:
        # person_is_infected and test_is_accurate?
        person_is_infected = random.random() < infection_rate
        test_is_accurate = random.random() < test_accuracy

        # Still inside the loop
        # - based on simulations, increment one of the four tallies.
        if person_is_infected and test_is_accurate: 
            true_pos += 1
        elif person_is_infected:    # test is not accurate
            false_neg += 1
        elif test_is_accurate:      # person is not infected
            true_neg += 1
        else:                       # person not infected, test not accurate
            false_pos += 1

    # After loop is done, print out the four values
    # what goes inside the parentheses? Repeat for each value
    print(f'True positives: {true_pos}') 
    print(f'False positives: {false_pos}')
    print(f'False negatives: {false_neg}')
    print(f'True negatives: {true_neg}')

    # Return the fraction of positive tests that were inaccurate
    # what goes here? What is the formula to use?
    return false_pos / (true_pos + false_pos)

def main():
    """
    Get user input about diagnostic and display percentage of false positives.
    
    Preconditions: None
    
    Postconditions: Percentage of false positives is displayed onscreen
    """
    # Get inputs
    num = int(input('Number of people: '))

    # Other inputs ...
    accuracy = float(input('Test accuracy: '))
    rate = float(input('Infection rate: '))

    # Call simulate_tests with the user inputs as arguments
    # and store returned value in a variable
    incorrect = simulate_tests(num, accuracy, rate) # remember the arguments!

    # Print the percentage of positive results that were incorrect
    # What goes inside the parentheses?
    print(f'{incorrect * 100 :.2f}% of positive tests were incorrect') 

# There is no need to edit code below this line
if __name__ == "__main__":
    main()