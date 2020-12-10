input = open('10dec.txt').read().split('\n')

adapters = sorted([int(num) for num in input if num.isdigit()])
adapters.insert(0, 0) 
adapters.append(adapters[-1] + 3)
seen_paths = {}

def part1():
    jolt_counter, nbr_1_jolt_diff, nbr_3_jolt_diff = 0,0,0

    for adapter in adapters:
        if adapter - jolt_counter == 1:
            nbr_1_jolt_diff += 1
        elif adapter - jolt_counter == 3:
            nbr_3_jolt_diff += 1
        jolt_counter = adapter

    print(nbr_1_jolt_diff * nbr_3_jolt_diff)

def find_path(i):
    if i == len(adapters)-1:
        return 1
    elif i in seen_paths:
        return seen_paths[i]
    ans = 0 
    for j in range(i+1, min(i+4, len(adapters))):
        if adapters[j] - adapters[i] <=3:
            ans += find_path(j)
    seen_paths[i] = ans
    return ans

def part2():
    print(find_path(0))

part1()
part2()