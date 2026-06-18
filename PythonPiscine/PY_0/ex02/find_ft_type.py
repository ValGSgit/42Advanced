
def all_thing_is_obj(obj: any) -> int:
    """Print obj type info and return 42."""
    # TODO: print the type of each known collection like this:
    #   list   -> "List : <class 'list'>"
    #   tuple  -> "Tuple : <class 'tuple'>"
    #   set    -> "Set : <class 'set'>"
    #   dict   -> "Dict : <class 'dict'>"
    #   str    -> "<value> is in the kitchen : <class 'str'>"
    #   other  -> "Type not found"
    # Then return 42 in all cases.
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
    return 42


# def check_with_type_dict(obj: any) -> int:
#     """Type check using dict + MRO — works for subclasses too."""
#     types = {
#         list: "List",
#         tuple: "Tuple",
#         set: "Set",
#         dict: "Dict",
#         str: f"{obj} is in the kitchen",
#     }
#     match = next((t for t in type(obj).__mro__ if t in types), None)
#     if match:
#         print(f"{types[match]} : {type(obj)}")
#     else:
#         print("Type not found")
#     return 42
 

    
