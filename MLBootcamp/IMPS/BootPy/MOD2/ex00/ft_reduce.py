
def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.

    Args:
        function_to_apply: a function taking two arguments.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.

    HINTS:
      - NOT a generator. This returns one value, so use `return`.
      - Get an iterator with `it = iter(iterable)`, pull the first element with
        `next(it)` to seed an accumulator.
      - Then loop the rest: `acc = function_to_apply(acc, elem)`.
      - Decide what to do if the iterable is empty (real reduce raises TypeError;
        `next()` on an empty iterator raises StopIteration you can catch).
    """
    it = iter(iterable)          # 1. get an iterator
    try:
        acc = next(it)           # 2. first element seeds the accumulator
    except StopIteration:
        return None              # empty iterable → return None (per docstring)
    for elem in it:              # 3. iterate over the REST
        acc = function_to_apply(acc, elem)
    return acc


def main():
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print("mine:")
    print(ft_reduce(lambda u, v: u + v, lst))


if __name__ == "__main__":
    main()
