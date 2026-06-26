def what_are_the_vars(*args, **kwargs):
    """Return an ObjectC instance carrying every received argument as an attr.

    HINTS:
      - Create an ObjectC instance first.
      - Loop `enumerate(args)` -> setattr(obj, f"var_{i}", value).
      - Loop `kwargs.items()` -> if the name already exists (hasattr) return None,
        otherwise setattr it.
      - Modify the instance, NOT the class.
    """
    # TODO: your code here
    obj = ObjectC()
    for i, value in enumerate(args):
        setattr(obj, f"var_{i}", value)
    for i, value in kwargs.items():
        if hasattr(obj, i):
            return None
        else:
            setattr(obj, i, value)
    return obj


class ObjectC(object):
    def __init__(self):
        # Nothing fixed here — attributes are added from outside via setattr.
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
