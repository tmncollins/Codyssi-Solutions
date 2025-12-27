from functools import lru_cache
from collections import defaultdict
import sys
f = open('inputs/input17.txt', 'r').read().strip().split('\n')

sys.setrecursionlimit(1000000000)
staircase = dict()
return_staircase = dict()
feeder_staircase = defaultdict(list)
for line in f:
    if len (line) < 3: break
    line = line.split()
    sc = line[0]; start = int(line[2]); end = int(line[4])
    sc_start = line[7]; sc_end = line[9]
    staircase[sc] = (start, end)
    if sc != 'S1':
        sc_from = line[7]; sc_to = line[9]
        feeder_staircase[(sc_from, start)].append(sc)
        return_staircase[sc] = sc_to

valid = f[-1].split(':')[1].split(',')
valid = list(map(int, valid))

@lru_cache(maxsize=None)
def part1(i):
    if i == staircase['S1'][1]: return 1
    if i > staircase['S1'][1]: return 0
    ans = 0
    for m in valid:
        ans += part1(i+m)
    return ans

print('Part 1:', part1(0))

#@lru_cache(maxsize=None)
def part2_helper(sc, i, m):
    if i > staircase[sc][1]: return set() # off end of staircase
    if m == 0: return {(sc, i)}
    # end of staircase?
    if i == staircase[sc][1]:
        if sc not in return_staircase: return set()
        return part2_helper(return_staircase[sc], i, m-1)
    ans = part2_helper(sc, i+1, m-1) # step 1 further
    if (sc, i) in feeder_staircase:
        for sc2 in feeder_staircase[(sc, i)]:
            ans2 = part2_helper(sc2, i, m-1) # swap staircase
            for j in ans2: ans.add(j)
    return ans

@lru_cache(maxsize=None)
def part2(sc, i):
    if i > staircase[sc][1]: return 0 # off end of staircase
    if sc == 'S1' and i == staircase[sc][1]: return 1 # end!

    ans = 0
    moves = set()
    for m in valid:
        for m2 in part2_helper(sc, i, m): moves.add(m2)
    for sc2, i2 in moves:
        ans += part2(sc2, i2)
    return ans

print('Part 2:', part2('S1', 0))

def part3(rank):
    ans = 'S1_0'
    pos = ('S1', 0)

    while True:
        # get places we can move to
        valid_moves = set()
        for v in valid:
            for m in part2_helper(pos[0], pos[1], v):
                SC, I = m
                valid_moves.add((int(SC[1:]), I, SC))
        valid_moves = sorted(list(valid_moves))

        for _, i, sc in valid_moves:
            x = part2(sc, i)
            if x >= rank:
                pos = (sc, i)
                ans += '-' + sc + '_' + str(i)
                break
            rank -= x

        if pos[0] == 'S1' and pos[1] == staircase['S1'][1]: return ans

print('Part 3:')
print(part3(100000000000000000000000000000))