"""
logical_operators.py

Check evaluation of boolean expressions using and, or, and not.

Programmer: Surajit A. Bose, Date: 2024.05.17
"""

def main():
    evaluate_and_print (False, False)
    evaluate_and_print (True, True)
    evaluate_and_print (True, False)
    evaluate_and_print (False, True)


def evaluate_and_print(x, y): 
    print(f"x = {x}, y = {y} : ")
    print(f"\t{'not x and y' : <15} {not x and y}")
    print(f"\t{'not (x and y)' : <15} {not (x and y)}")
    print(f"\t{'not x or y ' : <15} {not x or y}")
    print(f"\t{'not (x or y)' : <15} {not (x or y)}")
    print()


if __name__ == "__main__":
    main()
