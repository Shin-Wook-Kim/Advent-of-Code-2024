
map = []



with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day6/Day6Input1.txt", 'r') as file:
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




n_col = len(map[0])
n_row = len(map)

current = [-1,-1]

while(current[0] == -1):
    for i in range(n_row):
        for j in range(n_col):
            if map[i][j] in ['^','>','v','<']:
                current[0] = i
                current[1] = j

guard = True

i = current[0]
j = current[1]

counter = 0

while(guard):
    if map[i][j] == '^':
        if i == 0:
            map[i][j] = 'X'
            guard = False
        elif map[i-1][j] == '#':
            map[i][j] = '>'
        else:
            map[i-1][j] = '^'
            map[i][j] = 'X'
            i = i-1
    if map[i][j] == '>':
        if j == n_col-1:
            map[i][j] = 'X'
            guard = False
        elif map[i][j+1] == '#':
            map[i][j] = 'v'
        else:
            map[i][j+1] = '>'
            map[i][j] = 'X'
            j = j+1
    if map[i][j] == 'v':
        if i == n_row-1:
            map[i][j] = 'X'
            guard = False
        elif map[i+1][j] == '#':
            map[i][j] = '<'
        else:
            map[i+1][j] = 'v'
            map[i][j] = 'X'
            i = i+1
    if map[i][j] == '<':
        if j == 0:
            map[i][j] = 'X'
            guard = False
        elif map[i][j-1] == '#':
            map[i][j] = '^'
        else:
            map[i][j-1] = '<'
            map[i][j] = 'X'
            j = j-1
    counter += 1


visited = 0

for i in range(n_row):
    for j in range(n_col):
        if map[i][j] == 'X':
            visited += 1

print(visited)