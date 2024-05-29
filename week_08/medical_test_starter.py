import random

def simulate_tests(num_people, test_accuracy, infection_rate):
    """
    Params:
        num_people: the number of people getting the test 
        test_accuracy: how accurate the test is 
        infection_rate: the proportion of the population with the disease

    Return: fraction of positive results that are inaccurate
    """
    # We need to tally four values. 
    # Choose variable names for them and initialize to zero.
    true_pos = 0  # etc.

    # Loop over all individuals. 
    for i in range():  # what goes inside the parentheses?
        # Inside the loop:
        # - simulate whether the individual is infected
        # - simulate whether the test is accurate
        # - based on simulations, increment one of the four tallies.
    # Hint: The code 'is_true = random.random < 0.5' 
    # will set the variable 'is_true' to True 50% of the time.
    # How could you probabilistically set these two variables:
    # person_is_infected and test_is_accurate?

    # After loop is done, print out the four values
    print() # what goes inside the parentheses? Repeat for each value

    # Return the fraction of positive tests that were inaccurate
    return # what goes here? What is the formula to use?

def main():
    # Get inputs
    num = int(input('Number of people: '))
    # Other inputs ...

    # Call simulate_tests with the user inputs as arguments
    # and store returned value in a variable
    incorrect = simulate_tests() # remember the arguments!

    # Print the percentage of positive results that were incorrect
    print() # what goes inside the parentheses?

# There is no need to edit code below this line
if __name__ == "__main__":
    main()