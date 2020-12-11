from copy import deepcopy

input_lines = open('11dec.txt').read().split('\n')
input_lines = [list(line) for line in input_lines if line]

def next_state(input, part2):
    changed_state = False
    next_state = deepcopy(input)
    R, C = len(input), len(input[0])

    for row in range(R):
        for col in range(C):
            nbr_occ = 0 
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if not (dr==0 and dc==0):
                        row_dr = row + dr
                        col_dr = col + dc
                        while 0<=row_dr<R and 0<=col_dr<C and input[row_dr][col_dr]=='.' and part2:
                            row_dr = row_dr + dr
                            col_dr = col_dr + dc
                        if 0<=row_dr<R and 0<=col_dr<C and input[row_dr][col_dr]=='#':
                            nbr_occ += 1
            if input[row][col] == 'L':
                if nbr_occ == 0:
                    next_state[row][col] = '#'
                    changed_state = True
            elif input[row][col] == '#' and nbr_occ>=(5 if part2 else 4):
                next_state[row][col] = 'L'
                changed_state = True
    return next_state, changed_state

updated = True  
while updated:
    input_lines, updated = next_state(input_lines, part2=True)
sum = 0
for line in input_lines:
    sum += int(line.count('#'))
print(sum)