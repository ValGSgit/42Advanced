import sys


def main():
    """Check if the argument is odd or even."""
    # TODO:
    # 1. If more than one argument: print "AssertionError: more than one argument is provided"
    # 2. If no argument: do nothing (just exit)
    # 3. If argument is not an integer: print "AssertionError: argument is not an integer"
    # 4. If even: print "I'm Even."
    # 5. If odd:  print "I'm Odd."
    #
    # Hint: use assert and catch AssertionError
    # Hint: to check if a string is an integer (including negatives):
    #   arg.lstrip('-').isdigit()
    pass


if __name__ == "__main__":
    main()

# Test by running:
#   python whatis.py 14      -> I'm Even.
#   python whatis.py -5      -> I'm Odd.
#   python whatis.py         -> (nothing)
#   python whatis.py 0       -> I'm Even.
#   python whatis.py Hi!     -> AssertionError: argument is not an integer
#   python whatis.py 13 5    -> AssertionError: more than one argument is provided
