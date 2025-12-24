from copy import deepcopy

f = open('inputs/input12.txt', 'r').read().strip().split('\n')
status = 0

commands = []
grid = []
GRID = []
actions = []
MOD = 1073741824

for line in f:
    if len(line) < 3:
        status += 1
        continue
    if status == 0:
        GRID.append(list(map(int, line.split())))
    elif status == 1:
        commands.append(line.split())
    else:
        actions.append(line)

def output():
    global grid
    for line in grid:
        l = ''
        for x in line:
            l += str(x) + ' '
        print(l)
    print()

def f_all(op, v):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if op == 'mul': grid[y][x] *= v
            elif op == 'add': grid[y][x] += v
            elif op == 'sub': grid[y][x] -= v
            while grid[y][x] > MOD: grid[y][x] -= MOD
            while grid[y][x] < 0: grid[y][x] += MOD

def f_col(op, col, v):
    for y in range(len(grid)):
        if op == 'mul': grid[y][col] *= v
        elif op == 'add': grid[y][col] += v
        elif op == 'sub': grid[y][col] -= v
        while grid[y][col] > MOD: grid[y][col] -= MOD
        while grid[y][col] < 0: grid[y][col] += MOD

def f_row(op, row, v):
    for x in range(len(grid[0])):
        if op == 'mul': grid[row][x] *= v
        elif op == 'add': grid[row][x] += v
        elif op == 'sub': grid[row][x] -= v
        while grid[row][x] > MOD: grid[row][x] -= MOD
        while grid[row][x] < 0: grid[row][x] += MOD

def sum_row(row):
    return sum(grid[row])

def sum_col(col):
    tot = 0
    for y in range(len(grid)):
        tot += grid[y][col]
    return tot

def run(commands):
    global grid
    grid = deepcopy(GRID)

    for cmd in commands:
        if cmd[0] == 'SHIFT':
            if cmd[1] == 'ROW':
                row = int(cmd[2])-1
                x = int(cmd[4])
                for _ in range(x):
                    grid[row].insert(0, grid[row].pop())
            elif cmd[1] == 'COL':
                col = int(cmd[2])-1
                x = int(cmd[4])
                for _ in range(x):
                    val = grid[-1][col]
                    for i in range(len(grid)-1, 0, -1):
                        grid[i][col] = grid[i-1][col]
                    grid[0][col] = val

        elif cmd[0] == 'ADD':
            x = int(cmd[1])
            if cmd[2] == 'ALL': f_all('add', x)
            elif cmd[2] == 'COL': f_col('add', int(cmd[3])-1, x)
            elif cmd[2] == 'ROW': f_row('add', int(cmd[3])-1, x)

        elif cmd[0] == 'SUB':
            x = int(cmd[1])
            if cmd[2] == 'ALL': f_all('sub', x)
            elif cmd[2] == 'COL': f_col('sub', int(cmd[3])-1, x)
            elif cmd[2] == 'ROW': f_row('sub', int(cmd[3])-1, x)

        elif cmd[0] == 'MULTIPLY':
            x = int(cmd[1])
            if cmd[2] == 'ALL': f_all('mul', x)
            elif cmd[2] == 'COL': f_col('mul', int(cmd[3])-1, x)
            elif cmd[2] == 'ROW': f_row('mul', int(cmd[3])-1, x)
#        output()

def max_sum():
    part1 = 0
    for y in range(len(grid)):
        v = sum_row(y)
        part1 = max(part1, v)
    for x in range(len(grid[0])):
        v = sum_col(x)
        part1 = max(part1, v)
    return part1


# PART 1
run(commands)
print('Part 1:', max_sum())

# PART 2
new_commands = deepcopy(commands)
final_commands = []
take = []
for action in actions:
    if action == 'TAKE':
        take = new_commands.pop(0)
    elif action == 'CYCLE':
        new_commands.append(take)
    elif action == 'ACT':
        final_commands.append(take)
run(final_commands)
print('Part 2:', max_sum())

# PART 3
new_commands = deepcopy(commands)
final_commands = []
take = []
while new_commands:
    for action in actions:
        if action == 'TAKE':
            take = new_commands.pop(0)
        elif action == 'CYCLE':
            new_commands.append(take)
        elif action == 'ACT':
            final_commands.append(take)
            if len(new_commands) == 0: break
run(final_commands)
print('Part 3:', max_sum())


