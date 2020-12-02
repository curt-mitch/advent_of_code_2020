from collections import defaultdict
# https://adventofcode.com/2020/day/1
# find three values that sum to 2020
with open('day1_input.txt') as f:
    array = [int(line) for line in f]


def default_value():
    # use a dict to store value and differences
    return None


values = defaultdict(default_value)
answer = None
i = 0
while i < len(array) - 1:
    j = i + 1
    first_val = array[i]
    while j < len(array):
        second_val = array[j]
        diff = 2020 - (first_val + second_val)
        if (diff > 0):
            values[diff] = [first_val, second_val]
        j += 1
    i += 1

for num in array:
    if (values[num] is not None and
            num + values[num][0] + values[num][1] == 2020):
        answer = num * values[num][0] * values[num][1]
        # print(answer)
print(answer)
