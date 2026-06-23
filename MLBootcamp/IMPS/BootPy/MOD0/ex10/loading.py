import tqdm
from time import sleep

def ft_progress(lst):
    return tqdm.tqdm(lst)

def main(obj: None):
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.001)
    print()
    print(ret)

if __name__ == "__main__":
    main(None)