f = open('inputs/input10.txt', 'r').read().strip().split('\n')

for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))

def sum_row(y):
    tot = 0
    for x in range(len(f[y])):
        tot += f[y][x]
    return tot

def sum_col(x):
    tot = 0
    for y in range(len(f)):
        tot += f[y][x]
    return tot

def safest_path(start, end):
    dpmem = [[0 for _ in range(end[0]+1)] for _ in range(end[1]+1)]
    dpmem[start[1]][start[0]] = f[start[1]][start[0]]
    for y in range(start[1]+1, end[1]+1):
        dpmem[y][start[0]] = dpmem[y-1][start[0]] + f[y][start[0]]
    for x in range(start[0]+1, end[0]+1):
        dpmem[start[1]][x] = dpmem[start[1]][x-1] + f[start[1]][x]
    for y in range(start[1]+1, end[1]+1):
        for x in range(start[0]+1, end[0]+1):
            dpmem[y][x] = min(dpmem[y-1][x], dpmem[y][x-1]) + f[y][x]
    return dpmem[end[1]][end[0]]

best = float('inf')
for i in range(len(f)):
    x = sum_row(i)
    best = min(x, best)
    x = sum_col(i)
    best = min(x, best)

print('Part 1:', best)
print('Part 2:', safest_path((0,0), (14, 14)))
print('Part 3:', safest_path((0,0), (len(f[0])-1, len(f)-1)))
