f = open('inputs/input4.txt', 'r').read().strip().split()
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

part1 = 0
for line in f:
    for i in line:
        part1 += ALPHA.index(i)+1
print('Part 1:', part1)

part2 = 0
for line in f:
    keep = len(line) // 10
    line2 = line[:keep] + line[-keep:]
    for i in line2: part2 += ALPHA.index(i)+1
    x = str(len(line) - len(line2))
    for i in x: part2 += int(i)
print('Part 2:', part2)

part3 = 0
for line in f:
    last = ''
    line = line + '#'
    counter = 0
    for i in line:
        if i != last:
            if last != '':
                part3 += ALPHA.index(last)+1
                for j in str(counter): part3 += int(j)
            counter = 1
            last = i
        else: counter += 1
print('Part 3:', part3)
