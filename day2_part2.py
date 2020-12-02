# https://adventofcode.com/2020/day/2#part2

with open('day2_input.txt') as f:
    data = [line.split(':') for line in f]


def validatePasswords(char_range, pw):
    positions, sought_char = char_range.split(' ')
    # subtract 1 as positions are indexed starting at 1
    positions = list(map(lambda x: int(x) - 1, positions.split('-')))
    total_count = pw[positions[0]].count(sought_char)\
        + pw[positions[1]].count(sought_char)
    if total_count == 1:
        return True
    return False


valid_count = 0
for pw_pairs in data:
    if validatePasswords(pw_pairs[0], pw_pairs[1].strip()) is True:
        valid_count += 1

print(valid_count)
