from collections import defaultdict

f = open('inputs/input15.txt', 'r').read().strip().split('\n')
status = 0

artifacts = []
to_check = []
codes = dict()
for line in f:
    if len(line) < 3:
        status += 1
        continue
    if status == 0:
        code, ID = line.split(' | ')
        ID = int(ID)
        artifacts.append((code, ID))
        codes[ID] = code
    elif status == 1:
        code, ID = line.split(' | ')
        ID = int(ID)
        to_check.append((code, ID))
        codes[ID] = code

storage = [-1 for _ in range(1000000)]
for code, ID in artifacts:
    idx = 1
    while True:
        if storage[idx] == -1:
            storage[idx] = ID
            break
        if ID < storage[idx]: idx *= 2
        else:
            idx *= 2
            idx += 1

print(storage[:50])

layers = defaultdict(list)

def explore_storage(idx=1, depth=1):
    global storage, layers
    if storage[idx] == -1: return
    layers[depth].append(storage[idx])
    explore_storage(idx*2, depth + 1)
    explore_storage(idx*2+1, depth + 1)

explore_storage()

part1 = 0
l = 0
for v in (layers.values()):
    l += 1
    part1 = max(part1, sum(v))
part1 *= l
print('Part 1:', part1)

def get_ancestors(ID):
    seen = []
    idx = 1
    while True:
        if storage[idx] == -1:
            storage[idx] = ID
            break
        seen.append(codes[storage[idx]])
        if ID < storage[idx]:
            idx *= 2
        else:
            idx *= 2
            idx += 1
    return seen

print('Part 2:', '-'.join(get_ancestors(500000)))
ancestors_1, ancestors_2 = get_ancestors(to_check[0][1])[::-1], get_ancestors(to_check[1][1])[::-1]

for a in ancestors_1:
    if a in ancestors_2:
        print('Part 3:', a)
        break

