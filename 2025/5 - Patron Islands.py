f = open('inputs/input5.txt', 'r').read().strip().split('\n')

points = []
d_max = 0
d_min = float('inf')
for line in f:
    line = line[1:-1]
    p = list(map(int, line.split(',')))
    points.append(p)
    dist = abs(p[0]) + abs(p[1])
    d_max = max(d_max, dist)
    d_min = min(d_min, dist)

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def closest(point):
    distances = []
    for p in points:
        if p == point: continue
        distances.append((distance(p, point), p))
    distances.sort()
    return distances[0][1]

print('Part 1:', d_max - d_min)

p1 = closest((0,0))
p2 = closest(p1)
print('Part 2:', distance(p1, p2))

part3 = 0
p1 = (0,0)
while points:
    p2 = closest(p1)
    points.remove(p2)
    part3 += distance(p1, p2)
    p1 = p2
print('Part 3:', part3)
