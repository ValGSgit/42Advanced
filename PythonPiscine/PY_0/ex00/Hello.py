ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello": "titi!"}

# ===========================================================================
# LIST — ordered, mutable, allows duplicates
# ===========================================================================
print("=== LIST ===")
print("Access by index:       ", ft_list[0], ft_list[1])
print("Access by negative idx:", ft_list[-1])
print("Slice [0:1]:           ", ft_list[0:1])
print("Before mutation:       ", ft_list)

ft_list[1] = "World"           # mutate by index
ft_list.append("Extra")        # add to end
print("After [1]='World':     ", ft_list)
ft_list.remove("Extra")        # remove by value
print("Final:                 ", ft_list)

# ===========================================================================
# TUPLE — ordered, IMMUTABLE (can't change elements, must reassign whole thing)
# ===========================================================================
print("\n=== TUPLE ===")
print("Access by index:       ", ft_tuple[0], ft_tuple[1])
print("Access by negative idx:", ft_tuple[-1])
print("Slice [0:1]:           ", ft_tuple[0:1])
print("Before mutation:       ", ft_tuple)

# ft_tuple[1] = "Austria"  <- THIS WOULD CRASH: TypeError: 'tuple' object does not support item assignment
ft_tuple = ("Hello", "Austria")  # only way: reassign the whole variable
print("After reassign:        ", ft_tuple)

# ===========================================================================
# SET — unordered, mutable, NO duplicates, NO indexing
# ===========================================================================
print("\n=== SET ===")
print("Before mutation:       ", ft_set)

# ft_set[0]  <- THIS WOULD CRASH: TypeError: 'set' object is not subscriptable
ft_set.add("Vienna")
ft_set.remove("tutu!")
print("After add/remove:      ", ft_set)
ft_set.discard("nonexistent")  # remove if present, no error if missing
ft_set.add("Vienna")            # adding a duplicate — silently ignored
print("Adding duplicate Vienna:", ft_set)

# ===========================================================================
# DICT — key:value pairs, mutable, keys must be unique
# ===========================================================================
print("\n=== DICT ===")
print("Access by key:         ", ft_dict["Hello"])
print("Safe access (.get):    ", ft_dict.get("Hello"), ft_dict.get("missing", "default"))
print("Keys:                  ", list(ft_dict.keys()))
print("Values:                ", list(ft_dict.values()))
print("Before mutation:       ", ft_dict)

ft_dict["Hello"] = "42Vienna"  # mutate existing key
ft_dict["New"]   = "key"       # add a new key
print("After mutation:        ", ft_dict)
del ft_dict["New"]             # delete a key
print("After del:             ", ft_dict)

# ===========================================================================
# SUBJECT EXPECTED OUTPUT (the final values)
# ===========================================================================
print("\n=== Subject expected output ===")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

