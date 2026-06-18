def ft_filter(function, iterable):
    """Filter iterable — same behavior as the built-in filter(). Uses list comprehension."""
    # TODO: return a list of elements from iterable for which function returns True.
    # You MUST use a list comprehension (no for loop, no built-in filter).
    # Example: ft_filter(lambda x: x > 3, [1, 2, 3, 4, 5]) -> [4, 5]
    pass


def main():
    """Test ft_filter."""
    words = ["Hello", "World", "the", "a", "Python"]
    result = ft_filter(lambda x: len(x) > 4, words)
    print(result)
    # Expected: ['Hello', 'World', 'Python']

    nums = [1, 2, 3, 4, 5, 6]
    print(ft_filter(lambda x: x % 2 == 0, nums))
    # Expected: [2, 4, 6]


if __name__ == "__main__":
    main()
