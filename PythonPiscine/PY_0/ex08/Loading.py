import os


def ft_tqdm(lst: range) -> None:
    """Progress bar generator — clone of tqdm. Yields each element."""
    # TODO: for each element in lst:
    #   1. Calculate percent complete
    #   2. Get terminal width: os.get_terminal_size().columns
    #   3. Build bar string: "=" * filled + ">" + " " * remaining
    #   4. Print: "\r{percent}%|{bar}| {i+1}/{total}"  with end="" flush=True
    #   5. yield the element
    # After the loop: print() to move to next line
    pass
