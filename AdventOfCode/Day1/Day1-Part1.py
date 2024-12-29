# Day1: Part 1

import numpy as np

data = np.loadtxt("/Users/apple/Desktop/AdventOfCode/Day1/input.txt")

# Split the data into left and right lists
left, right = data[:, 0], data[:, 1]

# Sort both arrays
left.sort()
right.sort()

total_distance = int(np.sum(np.abs(left - right)))

print("Total distance:", total_distance)