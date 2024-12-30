maze = []


with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day16/Day16Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            temp = []
            for char in line:
                if not (char == '\n'):
                    temp.append(char)
            maze.append(temp)


nrow = len(maze)
ncol = len(maze[0])

current = (nrow-2,1,'>')



scores = []

initial = [[False for b in range(ncol)] for a in range(nrow)]

queue = [(nrow-2,1,'>',0)]

scoreboard = [[[-1,-1,-1,-1] for b in range(ncol)] for a in range(nrow)]



while (len(queue) > 0):
    stuff = queue.pop(0)
    i = stuff[0]
    j = stuff[1]
    d = stuff[2]
    cs = stuff[3]
    ns = 0
    if maze[i][j] == 'E':
        scores.append(cs)
    else:
        if d == '>':
            if (maze[i][j+1] != '#') and ((scoreboard[i][j+1][0] == -1) or (cs+1 <= scoreboard[i][j+1][0])):
                queue.append((i,j+1,'>', cs+1))
                scoreboard[i][j+1][0] = cs+1
            if (maze[i-1][j] != '#') and ((scoreboard[i-1][j][3] == -1) or (cs+1001 <= scoreboard[i-1][j][3])):
                queue.append((i-1,j,'^', cs+1001))
                scoreboard[i-1][j][3] = cs + 1001
            if (maze[i+1][j] != '#') and ((scoreboard[i+1][j][1] == -1) or (cs+1001 <= scoreboard[i+1][j][1])):
                queue.append((i+1,j,'v', cs+1001))
                scoreboard[i+1][j][1] = cs+1001
        if d == '<':
            if (maze[i][j-1] != '#') and ((scoreboard[i][j-1][2] == -1) or (cs+1 <= scoreboard[i][j-1][2])):
                queue.append((i,j-1,'<', cs+1))
                scoreboard[i][j-1][2] = cs+1
            if (maze[i-1][j] != '#') and ((scoreboard[i-1][j][3] == -1) or (cs+1001 <= scoreboard[i-1][j][3])):
                queue.append((i-1,j,'^', cs+1001))
                scoreboard[i-1][j][3] = cs+1001
            if (maze[i+1][j] != '#') and ((scoreboard[i+1][j][1] == -1) or (cs+1001 <= scoreboard[i+1][j][1])):
                queue.append((i+1,j,'v', cs+1001))
                scoreboard[i+1][j][1] = cs+1001
        if d == '^':
            if (maze[i-1][j] != '#') and ((scoreboard[i-1][j][3] == -1) or (cs+1 <= scoreboard[i-1][j][3])):
                queue.append((i-1,j,'^',cs+1))
                scoreboard[i-1][j][3] = cs+1
            if (maze[i][j+1] != '#') and ((scoreboard[i][j+1][0] == -1) or (cs+1001 <= scoreboard[i][j+1][0])):
                queue.append((i,j+1,'>',cs+1001))
                scoreboard[i][j+1][0] = cs+1001
            if (maze[i][j-1] != '#') and ((scoreboard[i][j-1][2] == -1) or (cs+1001 <= scoreboard[i][j-1][2])):
                queue.append((i,j-1,'<',cs+1001))
                scoreboard[i][j-1][2] = cs+1001
        if d == 'v':
            if (maze[i+1][j] != '#') and ((scoreboard[i+1][j][1] == -1) or (cs+1 <= scoreboard[i+1][j][1])):
                queue.append((i+1,j,'v', cs+1))
                scoreboard[i+1][j][1] = cs+1
            if (maze[i][j+1] != '#') and ((scoreboard[i][j+1][0] == -1) or (cs+1001 <= scoreboard[i][j+1][0])):
                queue.append((i,j+1,'>',cs+1001))
                scoreboard[i][j+1][0] = cs+1001
            if (maze[i][j-1] != '#') and ((scoreboard[i][j-1][2] == -1) or (cs+1001 <= scoreboard[i][j-1][2])):
                queue.append((i,j-1,'<',cs+1001))
                scoreboard[i][j-1][2] = cs+1001

        

print(scores)




