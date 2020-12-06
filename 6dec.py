input = open('6dec.txt').read().split('\n\n')

def part1():
    cnt = 0
    for group in input:
        groups_answers = group.split('\n')
        combined_ans = set(''.join(groups_answers))
        cnt = cnt + len(combined_ans)
    print(cnt)

def part2():
    cnt = 0
    for group in input:
        groups_answers = group.split('\n')
        for c in groups_answers[0]:
            if all(c in ans for ans in groups_answers[1:]):
                cnt += 1
    print(cnt)

part1()
part2()