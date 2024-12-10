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



def depth_count(pos):
    x = pos[0]
    y = pos[1]
    cur = top[x][y]
    nexts = []
    if cur == 9:
        return 1
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
            return 0
        else:
            sum = 0
            for next_p in nexts:
                sum += depth_count(next_p)
            return sum







sum = 0

for head in trailheads:
    sum += depth_count(head)

print(sum)