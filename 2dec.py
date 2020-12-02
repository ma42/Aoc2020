import re

input = open('2dec.txt')

def part1():
    valid_pwd = 0
    for line in input:
        tokens = re.split(' |: ', line)
        tokens[0] = list(map(int, tokens[0].split('-')))
        letters = list(filter(lambda c: (c == tokens[1]), tokens[2].strip('\n')))
        if tokens[0][0] <= len(letters) and len(letters) <= tokens[0][1]:
            valid_pwd += 1
    print(valid_pwd)

def part2():
    valid_pwd = 0
    for line in input:
        tokens = re.split(' |: ', line)
        tokens[0] = list(map(int, tokens[0].split('-')))
        pwd_letters = tokens[2].strip('\n')
        if pwd_letters[tokens[0][0]-1] == tokens[1] and not pwd_letters[tokens[0][1]-1] == tokens[1]:
            valid_pwd += 1
        elif not pwd_letters[tokens[0][0]-1] == tokens[1] and pwd_letters[tokens[0][1]-1] == tokens[1]:
            valid_pwd += 1
    print(valid_pwd)
