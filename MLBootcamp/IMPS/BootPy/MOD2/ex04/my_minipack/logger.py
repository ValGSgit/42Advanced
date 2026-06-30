import time
import os


def log(function):
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
        line = f"({username})Running:{name:<20}[ exec-time = {duration}]\n"
        with open("machine.log", "a") as f:
            f.write(line)
        return result
    return wrapper
