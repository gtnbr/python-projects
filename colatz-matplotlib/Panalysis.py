from matplotlib import pyplot as plt
import statistics
import random
from collections import Counter as ctr

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

y0 = []
y1 = []
y2 = []
y3 = []
y4 = []

for n in range(1, 1000001):
    # Plot for p = 0
    if random.random() > 0:
        c = collatz(n)
        y0.append(c)
    else:
        nc = not_collatz(n)
        y0.append(nc)
    # Plot for p = 0.25
    if random.random() > 0.25:
        c = collatz(n)
        y1.append(c)
    else:
        nc = not_collatz(n)
        y1.append(nc)
    # Plot for p = 0.5
    if random.random() > 0.5:
        c = collatz(n)
        y2.append(c)
    else:
        nc = not_collatz(n)
        y2.append(nc)
    # Plot for p = 0.75
    if random.random() > 0.75:
        c = collatz(n)
        y3.append(c)
    else:
        nc = not_collatz(n)
        y3.append(nc)
    # Plot for p = 1
    if random.random() > 1:
        c = collatz(n)
        y4.append(c)
    else:
        nc = not_collatz(n)
        y4.append(nc)

plt.figure(figsize=(12, 8))

colors = ["#ff0000", "#ff00ff", "#0000ff", "#00ffff", "#00ff00"]
mean0 = statistics.mean(y0)
std0 = statistics.stdev(y0)
m0 = ctr(y0)
x0 = list(m0.keys())
y0 = list(m0.values())
plt.scatter(x0, y0, color=colors[0], s=1, label = r"$p = 0$")
plt.axvline(x = mean0, color=colors[0])
plt.axvline(x = (mean0 + std0), color=colors[0], linestyle="dashed")
plt.axvline(x = (mean0 - std0), color=colors[0], linestyle="dashed")

mean1 = statistics.mean(y1)
std1 = statistics.stdev(y1)
m1 = ctr(y1)
x1 = list(m1.keys())
y1 = list(m1.values())
plt.scatter(x1, y1, color=colors[1], s=1, label = r"$p = 0.25$")
plt.axvline(x = mean1, color=colors[1])
plt.axvline(x = (mean1 + std1), color=colors[1], linestyle="dashed")
plt.axvline(x = (mean1 - std1), color=colors[1], linestyle="dashed")

mean2 = statistics.mean(y2)
std2 = statistics.stdev(y2)
m2 = ctr(y2)
x2 = list(m2.keys())
y2 = list(m2.values())
plt.scatter(x2, y2, color=colors[2], s=1, label = r"$p = 0.5$")
plt.axvline(x = mean2, color=colors[2])
plt.axvline(x = (mean2 + std2), color=colors[2], linestyle="dashed")
plt.axvline(x = (mean2 - std2), color=colors[2], linestyle="dashed")

mean3 = statistics.mean(y3)
std3 = statistics.stdev(y3)
m3 = ctr(y3)
x3 = list(m3.keys())
y3 = list(m3.values())
plt.scatter(x3, y3, color=colors[3], s=1, label = r"$p = 0.75$")
plt.axvline(x = mean3, color=colors[3])
plt.axvline(x = (mean3 + std3), color=colors[3], linestyle="dashed")
plt.axvline(x = (mean3 - std3), color=colors[3], linestyle="dashed")

mean4 = statistics.mean(y4)
std4 = statistics.stdev(y4)
m4 = ctr(y4)
x4 = list(m4.keys())
y4 = list(m4.values())
plt.scatter(x4, y4, color=colors[4], s=1, label = r"$p = 1$")
plt.axvline(x = mean4, color=colors[4])
plt.axvline(x = (mean4 + std4), color=colors[4], linestyle="dashed")
plt.axvline(x = (mean4 - std4), color=colors[4], linestyle="dashed")

plt.xlim(0, max(max(x0), max(x1), max(x2), max(x3), max(x4)))
plt.ylim(0, max(max(y0), max(y1), max(y2), max(y3), max(y4)))

plt.xlabel("Probabilistic Collatz Sequence Length", fontsize=14)
plt.ylabel("Multiplicity", fontsize=14)
plt.title("Multiplicty of Probabilistic Collatz Lengths from 1 to 1,000,000", fontsize=16)

plt.ticklabel_format(style='plain', axis='x')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend(fontsize=12)

plt.show()