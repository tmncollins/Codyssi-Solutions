f = open('inputs/input1.txt', 'r').read().strip().split('\n')
N = len(f)-1

compass = int(f[0])
offsets = ' ' + f[-1]
for i in range(1, N):
    if offsets[i] == '+': compass += int(f[i])
    else: compass -= int(f[i])

print('Part 1:', compass)

compass = int(f[0])
offsets = f[-1]
offsets = ' ' + offsets[::-1]
for i in range(1, N):
    if offsets[i] == '+': compass += int(f[i])
    else: compass -= int(f[i])

print('Part 2:', compass)

compass = int(f[0] + f[1])
offsets = f[-1]
offsets = ' ' + offsets[::-1]
for i in range(2, N, 2):
    num = int(f[i] + f[i+1])
    if offsets[i//2] == '+': compass += num
    else: compass -= num

print('Part 2:', compass)