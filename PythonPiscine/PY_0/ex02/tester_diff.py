from find_ft_type import all_thing_is_obj


def check_with_type_dict(obj: any) -> None:
    """Type check using type(obj) in dict — exact match only."""
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: f"{obj} is in the kitchen",
    }
    if type(obj) in types:
        print(f"{types[type(obj)]} : {type(obj)}")
    else:
        print("Type not found")


def check_with_isinstance(obj: any) -> None:
    """Type check using isinstance — catches subclasses too."""
    if isinstance(obj, list):
        print("List :", type(obj))
    elif isinstance(obj, tuple):
        print("Tuple :", type(obj))
    elif isinstance(obj, set):
        print("Set :", type(obj))
    elif isinstance(obj, dict):
        print("Dict :", type(obj))
    elif isinstance(obj, str):
        print(obj, "is in the kitchen :", type(obj))
    else:
        print("Type not found")


class MyList(list):
    """A custom list subclass."""
    pass


def main():
    """Show where type() dict and isinstance diverge."""
    print("=== Case 1: bool is a subclass of int ===")
    print("type(True) ==", type(True))       # <class 'bool'>
    print("isinstance(True, int) ==", isinstance(True, int))  # True
    print("dict approach  :", end=" ")
    check_with_type_dict(True)               # "Type not found" (bool not in dict)
    print("isinstance     :", end=" ")
    check_with_isinstance(True)              # also "Type not found" here (int not checked)

    print()
    print("=== Case 2: custom subclass of list ===")
    my_obj = MyList([1, 2, 3])
    print("type(my_obj) ==", type(my_obj))           # <class 'MyList'>
    print("isinstance(my_obj, list) ==", isinstance(my_obj, list))  # True
    print("dict approach  :", end=" ")
    check_with_type_dict(my_obj)             # "Type not found" (MyList not in dict)
    print("isinstance     :", end=" ")
    check_with_isinstance(my_obj)            # "List : <class '__main__.MyList'>"

    print()
    print("=== Case 3: normal cases (both behave identically) ===")
    for obj in [["a", "b"], ("x",), {1, 2}, {"k": "v"}, "Brian", 42]:
        print(f"  {repr(obj):<20} | dict: ", end="")
        check_with_type_dict(obj)
        print(f"  {repr(obj):<20} | isinstance: ", end="")
        check_with_isinstance(obj)


if __name__ == "__main__":
    main()
