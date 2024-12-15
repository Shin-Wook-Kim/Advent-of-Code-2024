map = []




with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day12/Day12Input1.txt", 'r') as file:
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
                    row.append(char)
            map.append(row)


n_row = len(map)
n_col = len(map[0])










plants = {}


for i in range(n_row):
    for j in range(n_col):
        plot = map[i][j]
        if plot in plants:
            plants[plot][i][j] = True
        else:
            new_m = [[False for b in range(n_col)] for a in range(n_row)]
            new_m[i][j] = True
            plants[plot] = new_m


h_regions = {}

for plant in plants:
    h_regions[plant] = [[] for a in range(n_row)]
    m = plants[plant]
    for i in range(n_row):
        for j in range(n_col):
            if m[i][j]:
                if h_regions[plant][i] == []:
                    h = [False for a in range(n_col)]
                    h[j] = True
                    h_regions[plant][i].append(h)
                else:
                    touching = False
                    for h in h_regions[plant][i]:
                        if h[j-1]:
                            h[j] = True
                            touching = True
                            break
                    if not touching:
                        h = [False for a in range(n_col)]
                        h[j] = True
                        h_regions[plant][i].append(h)


def find_maximal(hs,cgs):
    l = len(cgs)
    if l == 1:
        return hs,cgs
    for i in range(l):
        for j in range(l):
            if (j > i):
                temp = [x for x in cgs[i] if x in cgs[j]]
                if temp != []:
                    temp1 = []
                    for x in cgs[i]:
                        if not(x in temp1):
                            temp1.append(x)
                    for x in cgs[j]:
                        if not(x in temp1):
                            temp1.append(x)
                    temp2 = [hs[i][a] or hs[j][a] for a in range(n_col)]
                    hs2 = [hs[a] for a in range(len(hs)) if not((a == i) or (a == j))]
                    cgs2 = [cgs[a] for a in range(len(hs)) if not((a == i) or (a == j))]
                    cgs2.append(temp1)
                    hs2.append(temp2)
                    return find_maximal(hs2,cgs2)
    return hs,cgs









regions = {}

for plant in plants:
    regions[plant] = []
    groups = []
    for i in range(n_row):
        if groups == []:
            if not(h_regions[plant][i] == []):
                for h in h_regions[plant][i]:
                    m = [[False for a in range(n_col)] for b in range(n_row)]
                    for j in range(n_col):
                        m[i][j] = h[j]
                    groups.append(m)
        else:
            if h_regions[plant][i] == []:
                for m in groups:
                    regions[plant].append(m)
                groups = []
            else:
                cgs = []
                l = len(groups)
                for h in h_regions[plant][i]:
                    cg = []
                    for k in range(l):
                        for j in range(n_col):
                            if h[j] and groups[k][i-1][j]:
                                cg.append(k)
                                break
                    cgs.append(cg)
                if cgs == []:
                    for m in groups:
                        regions[plant].append(m)
                    groups = []
                    for h in h_regions[plant][i]:
                        m = [[False for a in range(n_col)] for b in range(n_row)]
                        for j in range(n_col):
                            m[i][j] = h[j]
                        groups.append(m)
                else:
                    mhs, mcgs = find_maximal(h_regions[plant][i], cgs)
                    groups2 = []
                    tcg = []
                    for k in range(len(mcgs)):
                        res = [[False for a in range(n_col)] for b in range(n_row)]
                        if mcgs[k] != []:
                            for a in mcgs[k]:
                                if not(a in tcg):
                                    tcg.append(a)
                                for p in range(n_row):
                                    for q in range(n_col):
                                        res[p][q] = res[p][q] or groups[a][p][q]
                        for j in range(n_col):
                            res[i][j] = mhs[k][j]
                        groups2.append(res)
                    ucg = [a for a in range(len(groups)) if not (a in tcg)]
                    for a in ucg:
                        regions[plant].append(groups[a])
                    groups = groups2
    if groups != []:
        for m in groups:
            regions[plant].append(m)







def find_cost(region):
    perimeter = 0
    area = 0
    for i in range(n_row):
        for j in range(n_col):
            if region[i][j]:
                area += 1
                if i == 0:
                    perimeter += 1
                else:
                    if not(region[i-1][j]):
                        perimeter += 1
                if i == (n_row - 1):
                    perimeter += 1
                else:
                    if not(region[i+1][j]):
                        perimeter += 1
                if j == 0:
                    perimeter += 1
                else:
                    if not(region[i][j-1]):
                        perimeter += 1
                if j == (n_col -1):
                    perimeter += 1
                else:
                    if not(region[i][j+1]):
                        perimeter += 1
    return perimeter * area



cost = 0



for plant in regions:
    for region in regions[plant]:
        cost += find_cost(region)



print(cost)







