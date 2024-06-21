'''
find_grandchildren.py

Given a dictionary with parent names as keys and that parent's children
as values, find each person's grandchildren if any.

Programmer: Surajit A. Bose, Date: 20240620
'''

SAMPLE_INPUT = {
    'Khaled': ['Chibundu', 'Jesmyn'],
    'Daniel': ['Khaled', 'Eve'],
    'Jesmyn': ['Frank'],
    'Eve': ['Grace']
}

def find_grandchildren(parents_dictionary):
    '''
    Params:
    parents_dictionary: a dictionary whose keys are strings representing 
        parent names and whose values are lists of that parent's children

    Returns: a dictionary mapping from people's names to lists
    of their grandchildren.
    '''
    grand_dict = {}
    for parent, children in parents_dictionary.items():
        for child in children:
            if child in parents_dictionary:
                if parent in grand_dict:
                    grand_dict[parent].extend(parents_dictionary[child])
                else:
                    grand_dict[parent] = parents_dictionary[child]
    return grand_dict

def main():
    grandchildren_dictionary = find_grandchildren(SAMPLE_INPUT)
    print(grandchildren_dictionary)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
