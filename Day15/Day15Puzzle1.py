warehouse = []
moves = []



with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day15/Day15Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    next = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        elif line == '\n':
            next = True
        else:
            if next:
                for char in line:
                    if not (char == '\n'):
                        moves.append(char)
            else:
                temp = []
                for char in line:
                    if not (char == '\n'):
                        temp.append(char)
                warehouse.append(temp)


nrow = len(warehouse)
ncol = len(warehouse[0])

current = (-1,-1)


for i in range(nrow):
    for j in range(ncol):
        if warehouse[i][j] == '@':
            current = (j,i)


def makemove(wh,m,c):
    res = wh
    j = c[0]
    i = c[1]
    if m == '>':
        if res[i][j+1] == '.':
            res[i][j+1] = '@'
            res[i][j] = '.'
            return res,(j+1,i)
        if res[i][j+1] == '#':
            return res,(j,i)
        if res[i][j+1] == 'O':
            k = j+1
            while k < ncol-1:
                if (res[i][k] == '.') or (res[i][k] == '#'):
                    break
                k += 1
            if res[i][k] == '#':
                return res,(j,i)
            else:
                while k > j+1:
                    res[i][k] = 'O'
                    k -= 1
                res[i][k] = '@'
                res[i][k-1] = '.'
                return res,(j+1,i)
    if m == '<':
        if res[i][j-1] == '.':
            res[i][j-1] = '@'
            res[i][j] = '.'
            return res,(j-1,i)
        if res[i][j-1] == '#':
            return res,(j,i)
        if res[i][j-1] == 'O':
            k = j-1
            while k > 0:
                if (res[i][k] == '.') or (res[i][k] == '#'):
                    break
                k -= 1
            if res[i][k] == '#':
                return res,(j,i)
            else:
                while k < j-1:
                    res[i][k] = 'O'
                    k += 1
                res[i][k] = '@'
                res[i][k+1] = '.'
                return res,(j-1,i)
    if m == 'v':
        if res[i+1][j] == '.':
            res[i+1][j] = '@'
            res[i][j] = '.'
            return res,(j,i+1)
        if res[i+1][j] == '#':
            return res,(j,i)
        if res[i+1][j] == 'O':
            k = i+1
            while k < nrow-1:
                if (res[k][j] == '.') or (res[k][j] == '#'):
                    break
                k += 1
            if res[k][j] == '#':
                return res,(j,i)
            else:
                while k > i+1:
                    res[k][j] = 'O'
                    k -= 1
                res[k][j] = '@'
                res[k-1][j] = '.'
                return res,(j,i+1)
    if m == '^':
        if res[i-1][j] == '.':
            res[i-1][j] = '@'
            res[i][j] = '.'
            return res,(j,i-1)
        if res[i-1][j] == '#':
            return res,(j,i)
        if res[i-1][j] == 'O':
            k = i-1
            while k > 0:
                if (res[k][j] == '.') or (res[k][j] == '#'):
                    break
                k -= 1
            if res[k][j] == '#':
                return res,(j,i)
            else:
                while k < i-1:
                    res[k][j] = 'O'
                    k += 1
                res[k][j] = '@'
                res[k+1][j] = '.'
                return res,(j,i-1)
        



for move in moves:
    warehouse,current = makemove(warehouse,move,current)



gps = 0

for i in range(nrow):
    for j in range(ncol):
        if warehouse[i][j] == 'O':
            gps += 100*i + j


print(gps)