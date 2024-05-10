"""
mars_weight.py

Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.

Surajit A. Bose
"""

# Gravity on Mars is lower, so a person would weigh 37.8% less than on Earth
MARS_WEIGHT_FACTOR = 0.378


def main():
    """Get Earth weight. Calculate and display Mars weight."""
    earth_weight = float(input('Enter a weight on Earth: '))
    mars_weight = round(earth_weight * MARS_WEIGHT_FACTOR, 2)
    print(f'The equivalent weight on Mars: {mars_weight}')
    
    
if __name__ == '__main__':
    main()