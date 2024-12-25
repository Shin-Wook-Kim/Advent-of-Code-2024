
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


def tree_like(hq):
    score = 0
    for i in range(nrow):
        for j in range(ncol):
            if (i + j <= 30) or (j - i >= 70):
                score += hq[i][j]
    if score < 20:
        return True







ebhq = [[0 for i in range(ncol)] for i in range(nrow)]



with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day14/Day14Output1.txt", 'w') as file:
    for k in range(100000):
        for i in range(nrow):
            for j in range(ncol):
                ebhq[i][j] = 0
        for robot in robots:
            x = (robot[0][0] + (k)*robot[1][0]) % ncol
            y = (robot[0][1] + (k)*robot[1][1]) % nrow
            ebhq[y][x] += 1
        if tree_like(ebhq):
            file.write(f'After {k} seconds\n')
            for i in range(nrow):
                temp = ''
                for j in range(ncol):
                    if ebhq[i][j] == 0:
                        temp += '.'
                    else:
                        temp += str(ebhq[i][j])
                temp += '\n'
                file.write(temp)
        

