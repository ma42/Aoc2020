import re, operator

lines = open('18dec.txt').read().strip().split('\n')
lines = [l.replace(' ','') for l in lines]
ops = { "+": operator.add, "*": operator.mul }
sum_ = 0
p1 = True

def evaluate(expr,p1):
    if p1:
        c = expr[0]
        for i in range(1,len(expr),2):
            c = ops[expr[i]](int(c), int(expr[i+1]))
        return c
    else:
        exp = []
        i=0
        while i < len(expr):
            c = expr[i]
            if not c == '+':
                exp.append(c)
                i+=1
            else:
                c = ops[c] (int(exp[-1]), int(expr[i+1]))
                exp[-1] = c
                i+=2
        ans = evaluate(exp,True)
        return ans

for line in lines:
    i=0
    stack = []
    while i < len(line):
        c=line[i]
        while not c==')' and i+1 < len(line):
            stack.append(c)
            i+=1
            c = line[i]
        if i==len(line)-1 and not c==')':
            stack.append(c)
        c_ = stack.pop()
        eval=[]
        while not c_ == '(' and stack:
            eval.insert(0,c_)
            c_ = stack.pop()
        if not stack and i==len(line)-1:
            eval.insert(0,c_)
        stack.append(evaluate(eval,p1))
        i+=1
        if i==len(line):
            eval = stack
            stack = []
            stack.append(evaluate(eval, p1))
    sum_ += stack[0]
print(sum_)
