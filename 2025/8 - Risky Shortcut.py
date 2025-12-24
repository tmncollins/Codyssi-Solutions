f = open('inputs/input8.txt', 'r').read().strip().split('\n')

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'

part1 = 0
for line in f:
    for i in line:
        if i in ALPHA: part1 += 1
print('Part 1:', part1)

part2 = 0
for line in f:
    line = list(line)
    while True:
        w = True
        for i in range(len(line)):
            if line[i] in NUMBERS:
                if i > 0 and line[i-1] not in NUMBERS:
                    line.pop(i-1)
                    line.pop(i-1)
                    w = False
                    break
                if i+1 < len(line) and line[i+1] not in NUMBERS:
                    line.pop(i)
                    line.pop(i)
                    w = False
                    break
        if w: break
    part2 += len(line)
print('Part 2:', part2)

part3 = 0
for line in f:
    line = list(line)
    while True:
        w = True
        for i in range(len(line)):
            if line[i] in NUMBERS:
                if i > 0 and line[i-1] in ALPHA:
                    line.pop(i-1)
                    line.pop(i-1)
                    w = False
                    break
                if i+1 < len(line) and line[i+1] in ALPHA:
                    line.pop(i)
                    line.pop(i)
                    w = False
                    break
        if w: break
    part3 += len(line)
print('Part 3:', part3)