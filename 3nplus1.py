import matplotlib
import matplotlib.pyplot as plt

max_seeds = 100

def threexplusone(num):
    if not (num % 2):
        return int(num / 2)
    else:
        return int(1 + num * 3)

sequence = list()

for seed in range(1, max_seeds+1):
    sequence.clear()
    x = seed
    while x != 1:
        sequence.append(x)
        x = threexplusone(x)
    sequence.append(1)
    plt.plot(sequence)

plt.show()
