"""
short_circuit.py

Demonstrate behavior of short circuit evaluation of booleans.

Programmer: Surajit A. Bose, Date: 2024.05.17
"""

def main():
    print(True or 'Hello')
    print(False or 'Hello')
    print(True and 'Hello')
    print(False and 'Hello')
    
if __name__ == '__main__':
    main()