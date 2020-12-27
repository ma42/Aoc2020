import itertools
from collections import defaultdict

input = open('17dec.txt').read().strip().split('\n')
init_state = [list(line) for line in input]

def solve(p1):
    active = set()
    for x,row in enumerate(init_state):
        for y,char in enumerate(row):
            if char == '#':
                active.add((x,y,0) if p1 else (x,y,0,0))   
    
    for _ in range(6):
        count_neigh = defaultdict(int)
        if p1:
            for (x,y,z) in active: 
                for dx,dy,dz in itertools.product([-1,0,1], repeat=3):
                    if (dx,dy,dz) == (0,0,0): continue
                    count_neigh[(x+dx, y+dy, z+dz)] += 1
        else:
            for (x,y,z,w) in active: 
                for dx,dy,dz,dw in itertools.product([-1,0,1], repeat=4):
                    if (dx,dy,dz,dw) == (0,0,0,0): continue
                    count_neigh[(x+dx, y+dy, z+dz, w+dw)] += 1
        active = {cube for cube,cnt in count_neigh.items() if cnt==3 or (cnt==2 and cube in active)}
    return len(active)

print("Part 1:",solve(p1=True))
print("Part 2:",solve(p1=False))

