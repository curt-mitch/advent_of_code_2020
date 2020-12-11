# https://adventofcode.com/2020/day/4
import re

with open('day4_input.txt') as f:
    # separate by blank lines
    data = f.read().split('\n\n')

prog = re.compile(r"[a-z]{3}\:")
match1 = ['byr:', 'cid:', 'ecl:', 'eyr:', 'hcl:', 'hgt:', 'iyr:', 'pid:']
match2 = ['byr:', 'ecl:', 'eyr:', 'hcl:', 'hgt:', 'iyr:', 'pid:']
valid_pp_count = 0

for passport_data in data:
    categories = sorted(prog.findall(passport_data))
    if categories == match1 or categories == match2:
        valid_pp_count += 1

print(valid_pp_count)
