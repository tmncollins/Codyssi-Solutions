status = 0
f = open('inputs/input7.txt', 'r').read().strip().split('\n')

TRACKS = []
swaps = []
target = 0
for line in f:
    if len(line) <= 1:
        status += 1
        continue
    if status == 0:
        TRACKS.append(int(line))
    elif status == 1:
        swaps.append(list(map(int, line.split('-'))))
    else:
        target = int(line)

tracks = list(TRACKS)
for a,b in swaps:
    a -= 1; b -= 1
    tracks[a], tracks[b] = tracks[b], tracks[a]

print('Part 1:', tracks[target-1])

tracks = list(TRACKS)
swaps.append(swaps[0])
for i in range(len(swaps)-1):
    a, b, c = swaps[i][0], swaps[i][1], swaps[i+1][0]
    a -= 1; b -= 1; c -= 1
    tracks[a], tracks[b], tracks[c] = tracks[c], tracks[a], tracks[b]

print('Part 2:', tracks[target-1])

tracks = list(TRACKS)
swaps.pop()
for a, b in swaps:
    a -= 1; b -= 1
    a,b = min(a,b), max(a,b)
    ai = a; bi = b
    while True:
        tracks[ai], tracks[bi] = tracks[bi], tracks[ai]
        ai += 1; bi += 1
        if ai >= b or bi >= len(tracks): break

print('Part 3:', tracks[target-1])


