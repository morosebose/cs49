"""
list_parameter.py

Demonstrate how passing a list as a parameter works

Programmer: Surajit A. Bose, Date: 2024.06.14
"""

def add_two_elements(some_list):
    """Accept a list as an input argument and add two elements at the end"""
    some_list.extend([6, 7])
    

def main():
    """Create a list with three elements. Use it as argument to a mutating function."""
    # create and print original list
    my_list = [1, 2, 3]
    print(f'Original list: {my_list}')
    
    # call mutating function
    print('Passing list as argument to mutating function')
    add_two_elements(my_list)
    
    # print list after call to mutating function
    print(f'Resultant list: {my_list}')