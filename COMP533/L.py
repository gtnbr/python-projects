from matplotlib import pyplot as plt
import statistics

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
mean = round(statistics.mean(y))
std = round(statistics.stdev(y))

# Create the plot with a larger figure size
plt.figure(figsize=(12, 8))  # Increased figure size for better readability

# Scatter plot and horizontal lines
plt.scatter(x, y, color="#0000ff", s=0.1)
plt.axhline(y=mean, color="#ff0000", label=rf"$\bar{{\mu}} = {mean}$")  # Mean with value
plt.axhline(y=(mean + std), color="#ff0000", linestyle="dashed", label=rf"$\bar{{\mu}} + \sigma = {mean + std}$")
plt.axhline(y=(mean - std), color="#ff0000", linestyle="dashed", label=rf"$\bar{{\mu}} - \sigma = {mean - std}$")

plt.xlim(0, max(x))
plt.ylim(0, max(y))

# Customize the axes
plt.xlabel("Starting Number", fontsize=14)
plt.ylabel("Collatz Sequence Length", fontsize=14)
plt.title("Collatz Lengths from 1 to 1,000,000", fontsize=16)

# Remove scientific notation from x-axis
plt.ticklabel_format(style='plain', axis='x')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the legend
plt.legend(fontsize=12)

# Display the plot
plt.show()
