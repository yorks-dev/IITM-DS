# Find the perimeter of a bar graph given the heights at each bar. Assume width of each bar is 1 unit and height is atleast 1 unit and the heights of each bar is given as integers.

# Input format

# First line will have the number of bar graphs, say n.
# Next n lines will have space seperated values
# Output format

# Perimeter of each bar graph printed over multiple lines
# Example

# 5 3 4 1 3 2 5

n = int(input())  # number of bar graphs

for i in range(n):
    perimeter = 0
    line = input().split(" ")

    perimeter += len(line) * 2 + int(line[0]) + int(line[len(line) - 1])

    for j in range(len(line) - 1):
        perimeter += abs(int(line[j]) - int(line[j + 1]))

    print(perimeter)
