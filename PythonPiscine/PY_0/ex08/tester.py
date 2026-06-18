from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print("Your ft_tqdm:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

print("Original tqdm:")
for elem in tqdm(range(333)):
    sleep(0.005)
print()

# Expected: both bars look nearly identical
# 100%|============================================>| 333/333
