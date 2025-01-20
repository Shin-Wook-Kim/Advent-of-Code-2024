bytes = []


with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day18/Day18Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            sline = line.split(',')
            bytes.append((int(sline[0]), int(sline[1])))




def canigetout (nrow,ncol,memsp):
    queue = [(0,0,0)]
    scoreboard = [[10000 for a in range(ncol)] for b in range(nrow)]
    scoreboard[0][0] = 0
    while (queue != []):
        v = queue.pop()
        if (v[1] == nrow-1) and (v[0] == ncol-1):
            return True
        if (v[0] > 0):
            if (scoreboard[v[1]][v[0]-1] > v[2]+1) and (memsp[v[1]][v[0]-1] == False):
                queue.insert(0,(v[0]-1,v[1],v[2]+1))
                scoreboard[v[1]][v[0]-1] = v[2]+1
        if (v[0] < ncol-1):
            if (scoreboard[v[1]][v[0]+1] > v[2]+1) and (memsp[v[1]][v[0]+1] == False):
                queue.insert(0,(v[0]+1,v[1],v[2]+1))
                scoreboard[v[1]][v[0]+1] = v[2]+1
        if (v[1] > 0):
            if (scoreboard[v[1]-1][v[0]] > v[2]+1) and (memsp[v[1]-1][v[0]] == False):
                queue.insert(0,(v[0],v[1]-1,v[2]+1))
                scoreboard[v[1]-1][v[0]] = v[2]+1
        if (v[1] < nrow-1):
            if (scoreboard[v[1]+1][v[0]] > v[2]+1) and (memsp[v[1]+1][v[0]] == False):
                queue.insert(0,(v[0],v[1]+1,v[2]+1))
                scoreboard[v[1]+1][v[0]] = v[2]+1
    return False



# nrow = 7
# ncol = 7

nrow = 71
ncol = 71

memspace = [[False for a in range(ncol)] for b in range(nrow)]

i = 0

while (i < 1024):
    memspace[bytes[i][1]][bytes[i][0]] = True
    i += 1

l = len(bytes)

while (i < l):
    memspace[bytes[i][1]][bytes[i][0]] = True
    if canigetout(nrow,ncol,memspace) == False:
        print(i)
        print(f"{bytes[i][0]},{bytes[i][1]}")
        break
    i += 1

print("done!")

    

