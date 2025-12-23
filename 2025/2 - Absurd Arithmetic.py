def fA_example(n):
    return n+495

def fB_example(n):
    return n*55

def fC_example(n):
    return n**3

def f_example(n):
    return fA_example(fB_example(fC_example(n)))

def fA(n):
    return n+724

def fB(n):
    return n*73

def fC(n):
    return n**3

def f(n):
    return fA(fB(fC(n)))

def median(items):
    items = sorted(items)
    return items[len(items)//2]

file = open('inputs/input2.txt', 'r').read().strip().split('\n')
file = list(map(int, file))

m = median(file)
print('Part 1:', m, f(m))

evens = 0
for n in file:
    if n%2 == 0: evens += n
print('Part 2:', evens, f(evens))

MAX = 15000000000000
best = 0
for i in file:
    price = f(i)
    if price < MAX and i > best:
        best = i
print('Part 3:', best)