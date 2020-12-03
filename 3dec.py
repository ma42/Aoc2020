import math

input = open('3dec.txt', 'r').read().splitlines()

def part1():
    i = 3
    tree_cnt = 0 
    for line in input[1:]:
        if line[i] == '#':
            tree_cnt += 1
        i = (i+3) % 31
    print(tree_cnt)

def part2():
    i,j,k,l,m = 1,3,5,7,1
    counter = [0]*5
    second_loop = 0

    for line in input[1:]:
        if line[i] == '#':
            counter[0] += 1
        if line[j] == '#':
            counter[1] += 1
        if line[k] == '#':
            counter[2] += 1
        if line[l] == '#':
            counter[3] += 1
        if second_loop:
            if line[m] == '#':
                counter[4] += 1
            m = (m+1) % 31
            
        i = (i+1) % 31
        j = (j+3) % 31
        k = (k+5) % 31
        l = (l+7) % 31
        second_loop = (second_loop+1) % 2

    print(math.prod(counter))

part1()
part2()
