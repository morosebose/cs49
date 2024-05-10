"""
mars_weight.py

Prompt the user for a weight on Earth and print the equivalent weight on Mars.

Programmer: Surajit A. Bose, Date: 2024.05.10
"""

# Gravity on Mars is lower, so a person would weigh 37.8% less than on Earth
MARS_CONVERSION_RATE = 0.378

def main():
    """
    Get Earth weight. Calculate and display Mars weight.
    
    Preconditions: None
    
    Postconditions: 
    - Earth weight received from user
    - Equivalent weight on Mars printed onscreen to two decimal places.
    """
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * MARS_CONVERSION_RATE
    mars_weight = round(mars_weight, 2)
    
    # Can combine the two previous steps into one
    # mars_weight = round(earth_weight * MARS_CONVERSION_RATE, 2)

    # print using f-strings
    print(f"The equivalent weight on Mars: {mars_weight}")

    # Two other ways to print: commas and plus signs
    # print("The equivalent weight on Mars:", mars_weight)
    # print("The equivalent weight on Mars: " + str(mars_weight))
    
if __name__ == '__main__':
    main()