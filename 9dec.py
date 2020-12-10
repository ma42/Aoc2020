input = open('9dec.txt').read().split('\n')
numbers = [int(num) for num in input if num.isdigit()]

def part1():
    for i, num in enumerate(numbers[25:]):
        found = False
        preamble = sorted(numbers[i:i+25])        
        j,k = 0, 24
        while j < k:
            if preamble[j] == preamble[k]:
                j += 1
            elif preamble[j] + preamble[k] == num:
                found = True
                break
            elif preamble[j] + preamble[k] < num:
                j += 1
            elif preamble[j] + preamble[k] > num:
                k -= 1
        if not found:
            print("Found num: {}".format(num))
            break

def part2():
    goal_num = 507622668
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            subset = numbers[i:j]
            if sum(subset) == goal_num:
                print(min(subset) + max(subset))
                break

part1()
part2()


