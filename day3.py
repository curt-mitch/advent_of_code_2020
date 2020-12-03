# https://adventofcode.com/2020/day/3
from functools import reduce

with open('day3_input.txt') as f:
    data = [line.strip() for line in f]


def count_trees(slope_map, down_move, right_move):
    i = down_move
    j = right_move
    tree_count = 0
    pattern_width = len(slope_map[0])
    while i < len(slope_map):
        if slope_map[i][j] == '#':
            tree_count += 1
        i += down_move
        j += right_move
        if j > (pattern_width - j):
            j = j % pattern_width
    return tree_count


# day 1 solution
print(count_trees(data, 1, 3))


# part 2
# https://adventofcode.com/2020/day/3#part2


slope_patterns = [  # [right move, down move]
  [1, 1],
  [1, 3],
  [1, 5],
  [1, 7],
  [2, 1]
]
tree_counts = []

for pattern in slope_patterns:
    tree_counts.append(count_trees(data, pattern[0], pattern[1]))

print(reduce((lambda x, y: x * y), tree_counts))
