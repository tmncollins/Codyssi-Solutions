from math import ceil

f = open('inputs\input11.txt', 'r').read().strip().split('\n')
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^'


def from_base(num, base):
    num = num[::-1]
    p = 1
    ans = 0
    for i in range(len(num)):
        ans += digits.index(num[i]) * p
        p *= base
    return ans

def to_base(num, base):
    p = 1
    while p <= num: p *= base
    p //= base
    ans = ''
    while p > 0:
        d = num // p
        ans += digits[d]
        num %= p
        p //= base
    return ans

part1 = 0
part2 = 0
for line in f:
    num, base = line.split()
    num = from_base(num, int(base))
    part1 = max(part1, num)
    part2 += num

print('Part 1:', part1)
print('Part 2:', to_base(part2, 68))

print('Part 3:', ceil(pow(part2, 1/4)))