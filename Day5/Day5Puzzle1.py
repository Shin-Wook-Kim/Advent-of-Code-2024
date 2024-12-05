
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

for update in updates:
    correct = True
    for rule in rules:
        a = rule[0]
        b = rule[1]
        if (a in update) and (b in update):
            a_ind = update.index(a)
            b_ind = update.index(b)
            if a_ind > b_ind:
                correct = False
                break
    if correct:
        sum += update[(len(update)-1) // 2 ]

print(sum)