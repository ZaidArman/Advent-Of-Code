# Day1: Part-2

with open("/Users/apple/Desktop/AdventOfCode/Day1/input.txt") as f:
    lines = f.read().strip().split("\n")

left = []
right = []

for line in lines:
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)

# Calculate the similarity score
similarity_score = 0
for num in left:
    count_in_right = right.count(num)
    similarity_score += num * count_in_right

print("Similarity Score:", similarity_score)