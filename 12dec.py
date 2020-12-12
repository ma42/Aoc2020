import numpy as np

input = open('12dec.txt').read().strip().split('\n')
convert = {0:'E', 90:'N', 180:'W', 270:'S'}

def part1():
    (x,y) = (0,0)
    d = 0
    for line in input:
        if line[0]=='F':
            line = line.replace('F',convert[d],1)
        if line[0] in ['N','S']:
            y = y + int(line[1:]) if line[0]=='N' else y - int(line[1:])
        elif line[0] in ['W','E']:
            x = x + int(line[1:]) if line[0]=='E' else x - int(line[1:])
        elif line[0] in ['L','R']:
            d = (d+int(line[1:]))%360 if line[0]=='L' else (d-int(line[1:]))%360
    print(abs(x) + abs(y))

def rotate(x,y,angle):
    theta = np.radians(angle)
    r = np.array(( (np.cos(theta), -np.sin(theta)), (np.sin(theta), np.cos(theta)) ))
    v = np.array((x,y))
    ans = r.dot(v)
    return int(np.rint(ans[0])), int(np.rint(ans[1]))

def part2():
    (sx,sy) = (0,0)
    (wx,wy) = (10,1)
    for line in input:
        if line[0]=='F':
            sx = sx + wx*int(line[1:])
            sy = sy + wy*int(line[1:])
        elif line[0] in ['N','S']:
            wy = wy + int(line[1:]) if line[0]=='N' else wy - int(line[1:])
        elif line[0] in ['W','E']:
            wx = wx + int(line[1:]) if line[0]=='E' else wx - int(line[1:])
        elif line[0] in ['R','L']:
            angle = int(line[1:]) if line[0]=='L' else -int(line[1:])
            wx, wy = rotate(wx,wy,angle)  
    print(abs(sx) + abs(sy))

part1()
part2()