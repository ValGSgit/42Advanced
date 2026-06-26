def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.

    Args:
        function_to_apply: a function taking one argument.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.

    HINTS:
      - Generator again (`yield`).
      - Loop over `iterable`; only `yield elem` when function_to_apply(elem)
        is truthy.
      - Bonus: the real filter accepts function=None, meaning "keep elements
        that are truthy by themselves". Handle it if you want to be thorough.
    """
    # TODO: your code here
    # ret = []
    for num in iterable:
        if function_to_apply(num) is True:
            yield num


def main():
    x = [1, 2, 3, 4, 5]
    print("mine:\n")
    print(ft_filter(lambda dum: not (dum % 2), x))
    print(list(ft_filter(lambda dum: not (dum % 2), x)))
    print("og:\n")
    print(filter(lambda dum: not (dum % 2), x))
    print(list(filter(lambda dum: not (dum % 2), x)))


if __name__ == "__main__":
    main()
