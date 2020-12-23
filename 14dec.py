import numpy as np
import re

input = open('14dec.txt').read().strip().split('\n')
reg = re.compile(r'mem\[(\d+)\]( = )?(\d*)')

def part1():
    mem = [0]*65499
    for line in input:
        if line.startswith('mask'):
            mask1 = int(line[7:].replace('X','1'), base=2)
            mask2 = int(line[7:].replace('X','0'), base=2)
        elif line.startswith('mem'):
            ins = reg.findall(line)
            mem[int(ins[0][0])] = (mask1 & int(ins[0][2])) | mask2
    print(sum(mem))

def float_address(mask, address, memory, value):
    if 'X' in mask:
        i = mask.index('X')
        float_address(mask[:i] +'0'+ mask[i+1:], address, memory, value)
        float_address(mask[:i] +'1'+ mask[i+1:], address, memory, value)
    else:
        mask = int(mask, base=2)
        memory[mask | address] = int(value)

def part2():
    mem, mask = {}, 0
    for line in input:
        ins, value = line.split(' = ')
        if ins=='mask':
            mask = value
        else: 
            address = int(reg.findall(ins)[0][0])
            address &= int(mask.replace("0", "1").replace("X", "0"), 2)
            float_address(mask, address, mem, value)
    print(sum(mem.values()))

part1()
part2()
