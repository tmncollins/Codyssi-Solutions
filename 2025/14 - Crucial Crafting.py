from functools import lru_cache
f = open('inputs/input14.txt', 'r').read().strip().split('\n')

items = []
for line in f:
    line = line.replace(',', '').split()
    quality, cost, unique_materials = int(line[5]), int(line[8]), int(line[12])
    items.append((quality, cost, unique_materials, line[1]))
items.sort()

part1 = 0
for i in range(5):
    part1 += items[-(i+1)][2]
print('Part 1:', part1)

best_quality = 0
best_materials = 0
best_items = []
part2 = 0

@lru_cache(maxsize=None)
def best_combination(to_spend, i=0):
    if i >= len(items):
        return 0, 0

    quality, materials = best_combination(to_spend, i+1)
    if to_spend >= items[i][1]:
        to_spend -= items[i][1]
        q, m = best_combination(to_spend, i+1)
        if q + items[i][0] > quality:
            quality = q + items[i][0]
            materials = m + items[i][2]
        elif q + items[i][0] == quality and m + items[i][2] < materials:
            quality = q + items[i][0]
            materials = m + items[i][2]


    return quality, materials

q, m = best_combination(30)
print('Part 2:', q*m)
q, m = best_combination(300)
print('Part 3:', q*m)
