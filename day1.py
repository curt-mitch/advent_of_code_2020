from collections import defaultdict
# https://adventofcode.com/2020/day/1
# find two values that sum to 2020
with open('day1_input.txt') as f:
    array = [int(line) for line in f]


def default_value():
    # use a dict to store value and differences
    return None


values = defaultdict(default_value)
answer = None
for val in array:
    difference = 2020 - val
    if values[val] is True:
        answer = val * difference
    else:
        values[difference] = True

print(answer)
