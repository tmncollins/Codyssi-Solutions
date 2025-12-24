from collections import defaultdict

f = open('inputs/input9.txt', 'r').read().strip().split('\n')

def run(PART=1):
    balances = dict()
    debts = defaultdict(list)
    status = 0

    for line in f:
        if len(line) < 3:
            status += 1
            continue
        if status == 0:
            line = line.split()
            balances[line[0]] = int(line[2])
        else:
            line = line.split()
            FROM = line[1]; TO = line[3]; AMOUNT = int(line[5])
            if PART == 2: AMOUNT = min(AMOUNT, balances[FROM])
            if PART == 3:
                if balances[FROM] < AMOUNT:
                    debts[FROM].append([AMOUNT-balances[FROM], TO])
                    AMOUNT = balances[FROM]
            balances[FROM] -= AMOUNT
            balances[TO] += AMOUNT
            if PART == 3:
                for TO in debts.keys():
                    # pay back debt
                    while balances[TO] > 0 and len(debts[TO]) > 0:
                        AMOUNT = min(balances[TO], debts[TO][0][0])
                        balances[TO] -= AMOUNT
                        balances[debts[TO][0][1]] += AMOUNT
                        debts[TO][0][0] -= AMOUNT
                        if debts[TO][0][0] == 0: debts[TO].pop(0)

    vals = sorted(balances.values())
    return vals[-1] + vals[-2] + vals[-3]

print('Part 1:', run())
print('Part 2:', run(PART=2))
print('Part 3:', run(PART=3))
