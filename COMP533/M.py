from matplotlib import pyplot as plt
import statistics
from collections import Counter as ctr

def collatz(n):
    list = []
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        list.append(n)
    return list

x = list(range(1, 1000001))
y = [len(collatz(n)) for n in x]
mean = statistics.mean(y)
std = statistics.stdev(y)
m = ctr(y)

x = list(m.keys())
y = list(m.values())

plt.figure(figsize=(12, 8))

plt.scatter(x, y, color="#ff0000", s=5)
plt.axvline(x = mean, color="#0000ff", label=rf"$\bar{{\mu}} = {round(mean, 3)}$")
plt.axvline(x = (mean + std), color="#0000ff", linestyle="dashed", label=rf"$\bar{{\mu}} + \sigma = {round(mean + std, 3)}$")
plt.axvline(x = (mean - std), color="#0000ff", linestyle="dashed", label=rf"$\bar{{\mu}} - \sigma = {round(mean - std, 3)}$")

plt.xlim(0, max(x))
plt.ylim(0, max(y))

# Customize the axes
plt.xlabel("Collatz Sequence Length", fontsize=14)
plt.ylabel("Multiplicity", fontsize=14)
plt.title("Multiplicty of Collatz Lengths from 1 to 1,000,000", fontsize=16)

# Remove scientific notation from x-axis
plt.ticklabel_format(style='plain', axis='x')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the legend
plt.legend(fontsize=12)

# Display the plot
plt.show()