import sys
from ft_filter import ft_filter


def main():
    """Filter words from S that are longer than N characters."""
    # TODO:
    # 1. Assert exactly 2 arguments are given and arg[1] is str, arg[2] is castable to int
    #    Print "AssertionError: the arguments are bad" if not
    # 2. S = sys.argv[1]  (the string)
    #    N = int(sys.argv[2])  (the minimum length)
    # 3. Split S into words (spaces only, no special chars)
    # 4. Use ft_filter + lambda to keep words with len > N
    # 5. Print the result list
    #
    # You MUST use at least one list comprehension and one lambda.
    pass


if __name__ == "__main__":
    main()

# Test by running:
#   python filterstring.py 'Hello the World' 4   -> ['Hello', 'World']
#   python filterstring.py 'Hello the World' 99  -> []
#   python filterstring.py 3 'Hello the World'   -> AssertionError: the arguments are bad
#   python filterstring.py                       -> AssertionError: the arguments are bad
