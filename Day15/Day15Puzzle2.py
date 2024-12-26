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
                    if (char == '#'):
                        temp.append('#')
                        temp.append('#')
                    if (char == 'O'):
                        temp.append('[')
                        temp.append(']')
                    if (char == '.'):
                        temp.append('.')
                        temp.append('.')
                    if (char == '@'):
                        temp.append('@')
                        temp.append('.')
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
        if res[i][j+1] == '[':
            k = j+1
            while k < ncol-1:
                if (res[i][k] == '.') or (res[i][k] == '#'):
                    break
                k += 1
            if res[i][k] == '#':
                return res,(j,i)
            else:
                while k > j+2:
                    res[i][k] = ']'
                    res[i][k-1] = '['
                    k -= 2
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
        if res[i][j-1] == ']':
            k = j-1
            while k > 0:
                if (res[i][k] == '.') or (res[i][k] == '#'):
                    break
                k -= 1
            if res[i][k] == '#':
                return res,(j,i)
            else:
                while k < j-2:
                    res[i][k] = '['
                    res[i][k+1] = ']'
                    k += 2
                res[i][k] = '@'
                res[i][k+1] = '.'
                return res,(j-1,i)
    if m == 'v':
        nsi = [[j]]
        nso = [['.']]
        k = i
        while k < nrow-1:
            k += 1
            tempi = []
            tempo = []
            for n in nsi[k-i-1]:
                if res[k][n] == '#':
                    return res,(j,i)
                if res[k][n] == '[':
                    tempi.append(n)
                    tempi.append(n+1)
                if res[k][n] == ']':
                    if not ((n-1) in tempi):
                        tempi.append(n-1)
                        tempi.append(n)
            if tempi == []:
                break
            else:
                for ind in tempi:
                    if ind in nsi[-1]:
                        if res[k-1][ind] == '@':
                            tempo.append('@')
                        if res[k-1][ind] == '[':
                            tempo.append('[')
                        if res[k-1][ind] == ']':
                            tempo.append(']')
                    else:
                        tempo.append('.')
                nsi.append(tempi)
                nso.append(tempo)
        l = len(nsi)
        for p in range(len(nsi[l-1])):
            res[i+l][nsi[l-1][p]] = res[i+l-1][nsi[l-1][p]]
        for p in range(l):
            if p < l-1:
                for q in range(len(nsi[p])):
                    if not(nsi[p][q] in nsi[p+1]):
                        res[i+p+1][nsi[p][q]] = res[i+p][nsi[p][q]]
            for q in range(len(nsi[p])):
                res[i+p][nsi[p][q]] = nso[p][q] 
        return res, (j,i+1)
    if m == '^':
        nsi = [[j]]
        nso = [['.']]
        k = i
        while k > 0:
            k -= 1
            tempi = []
            tempo = []
            for n in nsi[i-1-k]:
                if res[k][n] == '#':
                    return res,(j,i)
                if res[k][n] == '[':
                    tempi.append(n)
                    tempi.append(n+1)
                if res[k][n] == ']':
                    if not ((n-1) in tempi):
                        tempi.append(n-1)
                        tempi.append(n)
            if tempi == []:
                break
            else:
                for ind in tempi:
                    if ind in nsi[-1]:
                        if res[k+1][ind] == '@':
                            tempo.append('@')
                        if res[k+1][ind] == '[':
                            tempo.append('[')
                        if res[k+1][ind] == ']':
                            tempo.append(']')
                    else:
                        tempo.append('.')
                nsi.append(tempi)
                nso.append(tempo)
        l = len(nsi)
        for p in range(len(nsi[l-1])):
            res[i-l][nsi[l-1][p]] = res[i-l+1][nsi[l-1][p]]
        for p in range(l):
            if p < l-1:
                for q in range(len(nsi[p])):
                    if not(nsi[p][q] in nsi[p+1]):
                        res[i-p-1][nsi[p][q]] = res[i-p][nsi[p][q]]
            for q in range(len(nsi[p])):
                res[i-p][nsi[p][q]] = nso[p][q]
        return res, (j,i-1)
        


for i in range(nrow):
    temp = ''
    for j in range(ncol):
        temp += warehouse[i][j]
    print(temp)



for move in moves:
    warehouse,current = makemove(warehouse,move,current)
    # for i in range(nrow):
    #     temp = ''
    #     for j in range(ncol):
    #         temp += warehouse[i][j]
    #     print(temp)



gps = 0

for i in range(nrow):
    for j in range(ncol):
        if warehouse[i][j] == '[':
            gps += 100*i + j


print(gps)