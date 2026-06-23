import sys

class GotCharacter:
    def __init__(self, first_name, is_alive):
        try:
            self.first_name = first_name
            self.is_alive = is_alive
        except AssertionError as e:
            print(f"Error: {e}")
            sys.exit(1)

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    """The midget kingdom ig"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Jeoffrey got his balls stuck on the throne again"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

x = Stark("Poopoo")
b = Lannister("Ragnar", False)

# print(x)
# print(x.first_name)
# print(x.family_name)
# print(x.house_words)
# print(x.is_alive)
# x.die()
# print(x.is_alive)


# print()

# print(b)
# print(b.first_name)
# print(b.family_name)
# print(Lannister(b).house_words)
# print(b.is_alive)
# b.is_alive = True
# print(b.is_alive)
# b.die()
# print(b.is_alive)


# print(x.__dict__)
# print()
# print(b.__dict__)
# print()
# print(x.__doc__)
# print()
# print(b.__doc__)
