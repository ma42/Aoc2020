input = [1,2,16,19,18,0]
mem, spoken = {}, 0 
for i, num in enumerate(input[:-1]):
    mem[num] = i+1

p2 = False
for turn in range(7,(30000002 if p2 else 2022)):
    if spoken in mem.keys():
        tmp = spoken
        spoken = (turn-1) - mem[spoken]
        mem[tmp] = turn-1
    elif not spoken in mem.keys():
        mem[spoken] = turn-1
        spoken = 0 
    
for k in mem.keys():
    if mem[k] == (30000000 if p2 else 2020):
        print(k)