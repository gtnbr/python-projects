from matplotlib import pyplot as plt
import statistics
import random
from collections import Counter as ctr

p = 0.5

def collatz(n):
    length = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        length += 1
    return length

def not_collatz(n):
    length = 0
    vals = []
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n - 1
        if n in vals:
            break
        vals.append(n)
        length += 1
        if n == 1:
            break
    return length

y = []

for n in range(1, 1000001):
    if random.random() > p:
        c = collatz(n)
        y.append(c)
    else:
        nc = not_collatz(n)
        y.append(nc)

mean = statistics.mean(y)
std = statistics.stdev(y)
m = ctr(y)
x = list(m.keys())
y = list(m.values())

plt.figure(figsize=(12, 8))

plt.scatter(x, y, color="#0000ff", s=5)
plt.axvline(x = mean, color="#ff0000", label=rf"$\bar{{\mu}} = {round(mean, 3)}$")
plt.axvline(x = (mean + std), color="#ff0000", linestyle="dashed", label=rf"$\bar{{\mu}} + \sigma = {round(mean + std, 3)}$")
plt.axvline(x = (mean - std), color="#ff0000", linestyle="dashed", label=rf"$\bar{{\mu}} - \sigma = {round(mean - std, 3)}$")

plt.xlim(0, max(x))
plt.ylim(0, max(y))

# Customize the axes
plt.xlabel("Probabilistic Collatz Sequence Length", fontsize=14)
plt.ylabel("Multiplicity", fontsize=14)
plt.title("Multiplicty of Probabilistic Collatz Lengths from 1 to 1,000,000", fontsize=16)

# Remove scientific notation from x-axis
plt.ticklabel_format(style='plain', axis='x')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the legend
plt.legend(fontsize=12)

# Display the plot
plt.show()