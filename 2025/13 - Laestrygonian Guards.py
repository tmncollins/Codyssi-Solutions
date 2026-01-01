from collections import defaultdict, deque
from heapq import *
from random import shuffle
f = open('inputs/input13.txt', 'r').read().strip().split('\n')

graph = defaultdict(list)
for line in f:
    line = line.split()
    u, v, d = line[0], line[2], line[4]
    d = int(d)
    graph[u].append((v, d))
for u in graph:
    shuffle(graph[u])

def distances(PART=1, start='STT'):
    dists = dict()
    q = [(0, start)]
    while q:
        d, u = heappop(q)
        for v, _d in graph[u]:
            if PART == 1: _d = 1
            if v not in dists or (d + _d) < dists[v]:
                dists[v] = d + _d
                heappush(q, (d+_d, v))
    dists = sorted(dists.values())
    return dists[-1] * dists[-2] * dists[-3]

print('Part 1:', distances())
print('Part 2:', distances(PART=2))

def dfs_cycle(u, dist=0):
    global states, dists
    states[u] = 1

    longest = 0
    dists[u] = max(dists[u], dist)
    for v,d in graph[u]:
        if states[v] == 1:
            # cycles!
            longest = max(longest, dist - dists[v] + d)
        else:
            longest = max(longest, dfs_cycle(v, dist+d))
    states[u] = 2
    return longest


def longest_cycle(start):
    global states, dists
    states = {i:0 for i in graph.keys()}
    dists = {i:-1 for i in graph.keys()}
    return dfs_cycle(start)

part3 = 0
for u in graph.keys():
#    print(u, longest_cycle(u))
    part3 = max(part3, longest_cycle(u))
print('Part 3:', part3)