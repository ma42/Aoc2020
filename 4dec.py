import re

input = open('4dec.txt').read().split('\n\n')
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validation_rules = re.compile(r"byr:19[2-9]\d|200[0-2]|hcl:\#([0-9a-f]{6})|iyr:(201\d|2020)|hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)|pid:(\d{9}\b)|eyr:(202\d|2030)|ecl:(amb|blu|brn|gry|grn|hzl|oth)|cid:")

def part1():
    valid_cnt = 0
    for line in input:
        passport_fields = re.split(' |\n', line)
        fields = [field.split(':')[0] for field in passport_fields]
        valid = all(field in fields for field in required_fields)
        if valid:
            valid_cnt += 1
    print(valid_cnt)

def part2():
    valid_cnt = 0
    for line in input:
        passport_fields = re.split(' |\n', line)
        fields = [field.split(':')[0] for field in passport_fields]
        contains_all = all(field in fields for field in required_fields)
        if contains_all:
            valid = all([bool(re.search(validation_rules, field)) for field in passport_fields])
            if valid:
                valid_cnt += 1               
    print(valid_cnt)

part1()
part2()