
robots = []



with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day14/Day14Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            s_line = line.split()
            robot = []
            for i in range(2):
                a = s_line[i].find('=')
                b = s_line[i].find(',')
                robot.append((int(s_line[i][a+1:b]), int(s_line[i][b+1:])))
            robots.append(robot)



nrow = 103
ncol = 101

ebhq = [[0 for i in range(ncol)] for i in range(nrow)]

for robot in robots:
    x = (robot[0][0] + 100*robot[1][0]) % ncol
    y = (robot[0][1] + 100*robot[1][1]) % nrow
    ebhq[y][x] += 1

safety_factor = 1


temp = 0
for i in range(51):
    for j in range(50):
        temp += ebhq[i][j]
safety_factor *= temp


temp = 0
for i in range(51):
    for j in range(50):
        temp += ebhq[52+ i][j]
safety_factor *= temp


temp = 0
for i in range(51):
    for j in range(50):
        temp += ebhq[i][51+ j]
safety_factor *= temp


temp = 0
for i in range(51):
    for j in range(50):
        temp += ebhq[52+ i][51+ j]
safety_factor *= temp

print(safety_factor)