import re

rules, my_ticket, tickets = [line.split('\n') for line in open('16dec.txt').read().strip().split('\n\n')]
rules = { key : value.split(' or ') for (key,value) in [rule.split(': ') for rule in rules] }
rules = { k : [list(map(int,x.split('-'))) for x in v] for k,v in rules.items() }
tickets = [list(map(int,ticket.split(','))) for ticket in tickets[1:]]

p1_ans = 0
for ticket in tickets:
    for col in ticket:
        if not any(x[0]<=col<=x[1] or y[0]<=col<=y[1] for (x,y) in rules.values()): 
            p1_ans += col
print("Part 1: ", p1_ans)

valid_tickets = [ticket for ticket in tickets if 
                not any(not any(x[0]<=col<=x[1] or y[0]<=col<=y[1] for (x,y) in rules.values())
                for col in ticket)]

all_valid_classes = []
for i in range(len(rules)):
    valid_rule = set(rules.keys())
    for num in (ticket[i] for ticket in valid_tickets):
        valid_rule = { 
           k for k in valid_rule if any(lower <= num <= upper for lower,upper in rules[k])
        }
    all_valid_classes.append(valid_rule)

classes = [None for _ in range(len(rules))]
while None in classes:
    for i, v in enumerate(all_valid_classes):
        if classes[i] is not None: continue
        if len(v) == 1:
            classes[i] = next(iter(v))
            for j,u in enumerate(all_valid_classes):
                if j==i: continue
                if classes[i] in u: u.remove(classes[i])

p2_ans = 1
for rule, mine in zip(classes, my_ticket[1].split(',')):
    if rule.startswith('departure'):
        p2_ans *= int(mine)
print("Part 2: ", p2_ans)


