f = open('inputs/input6.txt', 'r').read().strip()

ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

part1 = 0
part2 = 0
values = []
for i in f:
    if i in ALPHA:
        part1 += 1
        part2 += ALPHA.index(i)+1
        values.append(ALPHA.index(i)+1)
    else: values.append(0)

print('Part 1:', part1)
print('Part 2:', part2)

part3 = 0
for i in range(len(values)):
    if values[i] > 0: part3 += values[i]
    else:
        values[i] = values[i-1]*2-5
        while values[i] > 52: values[i] -= 52
        while values[i] <= 0: values[i] += 52
        part3 += values[i]

print('Part 3:', part3)

