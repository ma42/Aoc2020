import itertools
import time

start_time = time.time()
input = open("1dec.txt", "r").read().split()
numbers = [int(nbr) for nbr in input]

def part1():
    for num1 in numbers:
        for num2 in numbers[1:]:
            if num1 + num2 == 2020:
                print(num1*num2)

def part2():
    # Alternative 1:
    # combinations = list(itertools.combinations(numbers, 3))
    # for triplet in combinations:
    #     if sum(triplet) == 2020:
    #         print(triplet[0]*triplet[1]*triplet[2])

    # Alternative 2 with lower time complexity:
    numbers.sort()
    for i, num1 in enumerate(numbers[0:len(numbers)-2]):
        k = len(numbers)-1
        j = i+1
        while j < k:
            triple_sum = sum([num1 + numbers[j] + numbers[k]])
            if triple_sum == 2020:
                print(num1 * numbers[j] * numbers[k])
                break
            elif triple_sum < 2020:
                j += 1
            else: 
                k -= 1
                
print("Runtime: {}".format(time.time() - start_time))