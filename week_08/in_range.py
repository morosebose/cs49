
def in_range(n, low, high):
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.
  """
  return low <= n <= high

# There is no need to edit code beyond this point

def main():
    """
    Gets user input for n, low, and high and then calls in_range.
    If n is in the range of low and high, print "n is in range!"
    if not print n is not in range...
    """
    num = int(input('n: '))
    low = int(input('low: '))
    high = int(input('high: '))

    if in_range(num, low, high):
        print('n is in range!')
    else:
        print('n is not in range...')



if __name__ == '__main__':
    main()