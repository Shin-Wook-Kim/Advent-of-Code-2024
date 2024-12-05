
rules = []

updates = []



with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day5/Day5Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    half = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
            continue
        if line == '\n':
            half = True
            continue
        if half:
            updates.append(list(map(int, line[:-1].split(sep = ','))))
        else:
            rules.append(list(map(int, line[:-1].split(sep = '|'))))

sum = 0


def fix(u,r):
    res = [0 for page in u]
    for page in u:
        temp = 0
        count = 0
        ind = 0
        for rule in r:
            if page in rule:
                ind += rule.index(page)
                temp += 1
        if temp == 0:
            res[-1-count] = page
            count += 1
        else:
            res[ind] = page
    return res


for update in updates:
    correct = True
    r_rules = []
    for rule in rules:
        a = rule[0]
        b = rule[1]
        if (a in update) and (b in update):
            r_rules.append(rule)
            a_ind = update.index(a)
            b_ind = update.index(b)
            if a_ind > b_ind:
                correct = False
    if not correct:
        res = fix(update,r_rules)
        sum += res[(len(res)-1) // 2 ]

print(sum)