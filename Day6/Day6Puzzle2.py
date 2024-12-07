
import copy


n_map = []



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
            n_map.append(row)




n_col = len(n_map[0])
n_row = len(n_map)

current = [-1,-1]

while(current[0] == -1):
    for i in range(n_row):
        for j in range(n_col):
            if n_map[i][j] in ['^','>','v','<']:
                current[0] = i
                current[1] = j

a = current[0]
b = current[1]
start = n_map[a][b]

def convert(char):
    if char == '^':
        return 0
    if char == '>':
        return 1
    if char == 'v':
        return 2
    else:
        return 3

def check_loop(map, current, orient):
    memory = []
    for i in range(n_row):
        memory.append([[False,False,False,False] for j in range(n_col)])
    guard = True
    i = current[0]
    j = current[1]
    map[i][j] = orient
    memory[i][j][convert(map[i][j])] = True
    while(guard):
        if map[i][j] == '^':
            if i == 0:
                map[i][j] = '.'
                guard = False
            elif map[i-1][j] == '#':
                map[i][j] = '>'
                memory[i][j][0] = True
            else:
                if memory[i-1][j][0]:
                    map[i][j] = '.'
                    break
                map[i-1][j] = '^'
                map[i][j] = '.'
                memory[i][j][0] = True
                i = i-1
        if map[i][j] == '>':
            if j == n_col-1:
                map[i][j] = '.'
                guard = False
            elif map[i][j+1] == '#':
                map[i][j] = 'v'
                memory[i][j][1] = True
            else:
                if memory[i][j+1][1]:
                    map[i][j] = '.'
                    break
                map[i][j+1] = '>'
                map[i][j] = '.'
                memory[i][j][1] = True
                j = j+1
        if map[i][j] == 'v':
            if i == n_row-1:
                map[i][j] = '.'
                guard = False
            elif map[i+1][j] == '#':
                map[i][j] = '<'
                memory[i][j][2] = True
            else:
                if memory[i+1][j][2]:
                    map[i][j] = '.'
                    break
                map[i+1][j] = 'v'
                map[i][j] = '.'
                memory[i][j][2] = True
                i = i+1
        if map[i][j] == '<':
            if j == 0:
                map[i][j] = '.'
                guard = False
            elif map[i][j-1] == '#':
                map[i][j] = '^'
                memory[i][j][3] = True
            else:
                if memory[i][j-1][3]:
                    map[i][j] = '.'
                    break
                map[i][j-1] = '<'
                map[i][j] = '.'
                memory[i][j][3] = True
                j = j-1
    return guard

loop_count = 0

for i in range(n_row):
    for j in range(n_col):
        if (not (i == current[0])) or (not (j == current[1])):
            if not(n_map[i][j] == '#'):
                n_map[i][j] = '#'
                print(i,j)
                if check_loop(n_map,[a,b],start):
                    loop_count += 1
                n_map[i][j] = '.'

print(loop_count)