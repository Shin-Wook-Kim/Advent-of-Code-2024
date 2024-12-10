top = []



with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day10/Day10Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            row = []
            for char in line:
                if not(char == '\n'):
                    row.append(int(char))
            top.append(row)



n_row = len(top)
n_col = len(top[0])

trailheads = []

for i in range(n_row):
    for j in range(n_col):
        if top[i][j] == 0:
            trailheads.append((i,j))


def depth_search(pos,dests):
    x = pos[0]
    y = pos[1]
    cur = top[x][y]
    nexts = []
    if cur == 9:
        res = dests + [(x,y)]
        return res
    else:
        if (x > 0):
            next = top[x-1][y]
            if (cur < next) and (next < cur + 2):
                nexts.append((x-1,y))
        if (x < n_row -1):
            next = top[x+1][y]
            if (cur < next) and (next < cur + 2):
                nexts.append((x+1,y))
        if (y > 0):
            next = top[x][y-1]
            if (cur < next) and (next < cur + 2):
                nexts.append((x,y-1))
        if (y < n_col - 1):
            next = top[x][y+1]
            if (cur < next) and (next < cur + 2):
                nexts.append((x,y+1))
        if nexts == []:
            res = dests
            return res
        else:
            res = dests
            for next_p in nexts:
                res = res + depth_search(next_p,dests)
            return res

sum = 0

for head in trailheads:
    dests = []
    dests = depth_search(head, dests)
    u_dests = []
    if dests == []:
        continue
    else:
        for dest in dests:
            if dest in u_dests:
                continue
            else:
                u_dests.append(dest)
    sum += len(u_dests)

print(sum)