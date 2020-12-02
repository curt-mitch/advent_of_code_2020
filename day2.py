# https://adventofcode.com/2020/day/2

with open('day2_input.txt') as f:
    data = [line.split(':') for line in f]


def validatePasswordPolicy(pattern, password):
    char_range, sought_char = pattern.split(' ')
    char_range = list(map(lambda x: int(x), char_range.split('-')))
    char_count = password.count(sought_char)
    # add 1 for inclusivity
    if char_count in range(char_range[0], char_range[1] + 1):
        return True
    return False


valid_count = 0
for pw_pair in data:
    if validatePasswordPolicy(pw_pair[0], pw_pair[1].strip()) is True:
        valid_count += 1

print(valid_count)
