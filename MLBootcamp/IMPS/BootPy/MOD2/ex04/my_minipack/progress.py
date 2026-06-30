from time import time


def ft_progress(lst):
    start = time()
    total = len(lst)
    for i, elem in enumerate(lst):
        elapsed = time() - start
        percent = (i + 1) / total
        eta = elapsed / (i + 1) * (total - i - 1) + elapsed
        bar_len = 40
        filled = int(bar_len * percent)
        bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        msg = f"\rETA: {eta:5.2f}s [{percent:>4.0%}][{bar}] {i+1}/{total} | elapsed time {elapsed:f}s"
        print(msg, end="")
        yield elem
