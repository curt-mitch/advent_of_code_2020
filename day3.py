# https://adventofcode.com/2020/day/3

with open('day3_input.txt') as f:
    data = [line.strip() for line in f]


i = 1
j = 3
tree_count = 0
pattern_width = len(data[0])
while i < len(data):
    if data[i][j] == '#':
        tree_count += 1
    i += 1
    j += 3
    if j > (pattern_width - j):
        j = j % pattern_width

print(tree_count)
