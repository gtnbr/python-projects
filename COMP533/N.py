from matplotlib import pyplot as plt
import statistics

def not_collatz(n):
    my_ans = ["red", 0]
    my_list = [n]
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n - 1
        if n in my_list:
            my_ans[0] = "red"
            break
        my_list.append(n)
        if n == 1:
            my_ans[0] = "blue"
            break
    my_ans[1] = len(my_list)
    return my_ans

x = range(1,1000001)
all_lengths = []
red_lengths = {}
blue_lengths = {}
for i in range (1, 1000001):
    my_ans = not_collatz(i)
    all_lengths.append(my_ans[1])
    if my_ans[0] == "red":
        red_lengths[i] = my_ans[1]
    if my_ans[0] == "blue":
        blue_lengths[i] = my_ans[1]


# Create the plot with a larger figure size
plt.figure(figsize=(12, 8))  # Increased figure size for better readability

# Scatter plot and horizontal lines
plt.scatter(blue_lengths.keys(), blue_lengths.values(), color="#0000ff", s=0.1, label = "Paths to 1")
plt.scatter(red_lengths.keys(), red_lengths.values(), color="#ff0000", s=0.1, label = "Paths that loop")

plt.xlim(0, max(x))
plt.ylim(0, max(all_lengths))

# Customize the axes
plt.xlabel("Starting Number", fontsize=14)
plt.ylabel("Modified Collatz Sequence Length", fontsize=14)
plt.title(r"Modified Collatz $(3n-1)$ Lengths from 1 to 1,000,000", fontsize=16)

# Remove scientific notation from x-axis
plt.ticklabel_format(style='plain', axis='x')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the legend
plt.legend(fontsize=12)

# Display the plot
plt.show()