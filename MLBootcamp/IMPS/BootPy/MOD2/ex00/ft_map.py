def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.

    Args:
        function_to_apply: a function taking one argument.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.

    HINTS:
      - Make this a generator: use `yield`, so calling it returns a generator
        object immediately (matches the <generator object ...> in the example).
      - Loop over `iterable`, and for each element yield function_to_apply(elem).
      - Optionally guard with `callable(function_to_apply)` and raise TypeError,
        like the real map does for a non-function.
    """
    for thing in iterable:
        if callable(function_to_apply):
            yield function_to_apply(thing)
        else:
            raise TypeError


def main():
    x = [1, 2, 3, 4, 5]
    print("mine:\n")
    print(ft_map(lambda dum: dum + 1, x))
    print(list(ft_map(lambda t: t + 1, x)))
    print("og:\n")
    print(map(lambda dum: dum + 1, x))
    print(list(map(lambda t: t + 1, x)))

if __name__ == "__main__":
    main()
