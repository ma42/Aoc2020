input = open('13dec.txt').read().strip().split('\n')

def part1():
    timestamp, bus_IDs = int(input[0]), [int(ID) for ID in input[1].replace('x,','').split(',')]
    next_dep = []
    for bus_id in bus_IDs:
        next_dep.append(bus_id - (timestamp%bus_id))
    wait_time = min(next_dep)
    best_bus = bus_IDs[next_dep.index(wait_time)]
    print(wait_time * best_bus)

def part2():
    ids = input[1].split(',')
    delta = []
    for i,id in enumerate(ids):    
        if not id == 'x':
            delta.append((int(id), i))

    step, t = delta[0][0], 0
    for id, offset in delta[1:]:
        while not (t + offset) % id == 0:        
            t += step
        step *= id
    print(t)

part1()
part2()