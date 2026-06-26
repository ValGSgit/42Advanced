import time
from random import randint
import os


def log(function):
    """Decorator that appends a timed entry to machine.log on every call.
    """
    def wrapper(*args, **kwargs):
        username = os.environ.get("USER", "unknown")
        start = time.time()
        name = function.__name__.replace("_", " ").title()
        result = function(*args, **kwargs)
        elapsed = time.time() - start
        if elapsed >= 1:
            duration = f"{elapsed:.3f} s"
        else:
            duration = f"{elapsed * 1000:.3f} ms"
        line = f"({username})Running:{f'{name}':<20}[ exec-time = {duration}]\n"
        with open("machine.log", "a") as f:
            f.write(line)
        return result
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
