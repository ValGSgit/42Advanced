# import tqdm
from time import time, sleep

"""next(x): runs the generator until it hits the next yield and returns the value, then pauses

e.g:
    gen = count()
    print(next(gen))   # runs to "yield 1", returns 1, pauses
    print(next(gen))   # resumes, runs to "yield 2", returns 2, pauses
    print(next(gen))   # resumes, runs to "yield 3", returns 3, pauses
    print(next(gen))   # nothing left -> raises StopIteration

A for loop is a next() in a loop?

    for elem in count():
        print(elem)

is basically:

    gen = count()
    while True:
        try:
            elem = next(gen)   # <-- get next value
        except StopIteration:  # <-- generator exhausted
            break
        print(elem)

"""

def ft_progress(lst):
    """A normal function returns once and forgets, with yield it becomes a generator
        That means it can pause, return a value and later continue where it left off as it was
        (e.g ft_progress() should return a generator object waiting to be continued)"""
    start = time()
    total = len(lst)
    for i, elem in enumerate(lst):
        elapsed = time() - start
        if i == int(len(lst) / 10):
            calc = (elapsed / (i + 1) * (total - i - 1) + elapsed)
            print(f"\nPredicted ETA after 1/10: {calc}\n")
            #because sleep slop, OS scheduling, and terminal I/O differ run to run#
        percent = (i + 1) / total
        eta = (elapsed / (i + 1) * (total - i - 1) + elapsed)
        bar_len = 40
        filled = int(bar_len * percent)
        bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        """print with carriage return and end so it overwrites the progress instead of line by line"""
        print(f"\rETA: {eta:5.2f}s [{percent:>4.0%}][{bar}] {i+1}/{total} | elapsed time {elapsed:f}s", end="")
        yield elem #return elem to caller loop
    

def main(obj=None):
    listy = range(3333)
    ret = 0
    sleepfor = 0.005
    estimate = ((len(listy) * sleepfor))
    print(f"\nPredicted total time: ~{(estimate):.2f}s (lower bound; real run is a bit higher)\n")
    for elem in ft_progress(listy):
        ret += elem
        sleep(sleepfor)
    print()
    print(ret)



if __name__ == "__main__":
    main(None)