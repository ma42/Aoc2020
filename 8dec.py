import re, operator
from copy import deepcopy

input = open('8dec.txt','r')
instructions = []
ops = { "+": operator.add, "-": operator.sub }

for line in input:
    instruction = line.strip('\n').split() 
    instructions.append(instruction)

def part1():
    program_counter, accumulator = 0,0
    executed_instructions = set()

    while not program_counter in executed_instructions:
        current = instructions[program_counter]
        opcode, op, ins  = current[0], current[1][0], int(current[1][1:])
        executed_instructions.add(program_counter)
        
        if opcode == 'acc':
            accumulator = ops[op](accumulator, ins) 
            program_counter += 1
        elif opcode == 'jmp':
            program_counter = ops[op](program_counter, ins)
        elif opcode == 'nop':
            program_counter += 1
        else: raise TypeError("Got unknown instruction")
    
    print(accumulator)


def part2():
    number_instructions = len(instructions)
    altered_instructions = list()

    for i in range(number_instructions):
        executed_instructions = set()
        program_counter, accumulator = 0,0
        
        altered_opcode = instructions[i][0]
        if altered_opcode == 'jmp':
            altered_opcode = 'nop'            
        elif altered_opcode == 'nop':
            altered_opcode = 'jmp'

        altered_instructions = deepcopy(instructions)
        altered_instructions[i][0] = altered_opcode

        while program_counter < number_instructions:
            current = altered_instructions[program_counter]
            opcode, op, ins  = current[0], current[1][0], int(current[1][1:])
            
            if program_counter in executed_instructions:
                break
            executed_instructions.add(program_counter)
            if opcode == 'acc':
                accumulator = ops[op](accumulator, ins) 
                program_counter += 1
            
            elif opcode == 'jmp':
                program_counter = ops[op](program_counter, ins)
            
            elif opcode == 'nop':
                program_counter += 1

            else: raise TypeError("Got unknown instruction")

            if program_counter == number_instructions:
                print(accumulator)
                break

        
part1()
part2()

