f = open('inputs/input3.txt', 'r').read().strip().split('\n')

part1 = 0
for line in f:
    a, b = line.split(' ')
    for rng in [a,b]:
        l,r = list(map(int, rng.split('-')))
        part1 += r+1-l
print('Part 1:', part1)

def condense_ranges(a, b):
    if a > b: return condense_ranges(b,a)
    if a[0] <= b[0] <= a[1]: return [[min(a[0], b[0]), max(a[1], b[1])]]
    return [a, b]

part2 = 0
for line in f:
    a, b = line.split(' ')
    a = list(map(int, a.split('-')))
    b = list(map(int, b.split('-')))
    for rng in condense_ranges(a, b):
        l, r = rng
        part2 += r + 1 - l
#    print(r+1-l)
print('Part 2:', part2)

part3 = 0
for i in range(1, len(f)):
    a, b = f[i].split(' ')
    c, d = f[i-1].split(' ')
    ranges = []
    for r in [a,b,c,d]:
        r = list(map(int, r.split('-')))
        ranges.append(r)
    ranges.sort()
#    print(ranges, end='    ')
    new_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        r = condense_ranges(new_ranges[-1], ranges[i])
        if len(r) == 1: new_ranges[-1] = r[0]
        else: new_ranges.append(r[1])
    boxes = 0
#    print(new_ranges)
    for rng in new_ranges:
        l, r = rng
        boxes += r + 1 - l
    part3 = max(part3, boxes)
print('Part 3:', part3)

