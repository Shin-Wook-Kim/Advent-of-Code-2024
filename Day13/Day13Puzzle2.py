

machines = []




with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day13/Day13Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    temp = []
    while (not done):
        line = file.readline()
        if line == '':
            done = True
            machines.append(temp)
        elif line == '\n':
            machines.append(temp)
            temp = []
        else:
            s_line = line.split()
            if s_line[0] == 'Button':
                temp.append(int(s_line[2][2:-1]))
                temp.append(int(s_line[3][2:]))
            else:
                temp.append(int(s_line[1][2:-1])+10000000000000)
                temp.append(int(s_line[2][2:])+10000000000000)




fewest = 0

for machine in machines:
    x1 = machine[0]
    y1 = machine[1]
    x2 = machine[2]
    y2 = machine[3]
    x3 = machine[4]
    y3 = machine[5]
    sol = (-1,-1)
    if x1 * y2 == x2 * y1:
        if x1 * y3 == x3 * y1:
            if x1 > 3*x2:
                if (x3 - (x3 // x1)*x1) % x2 == 0:
                    sol = (x3 // x1, (x3 - (x3 // x1)*x1) // x2)
            else:
                if (x3 - (x3 // x2) * x2) % x1 == 0:
                    sol = ((x3 - (x3 // x2)*x2) // x1, x3 // x2)
    else:
        if (y1*x3 -x1*y3) % (y1*x2 - x1*y2) == 0:
            b = (y1*x3-x1*y3) // (y1*x2-x1*y2)
            if (x3 - x2 * b) % x1 == 0:
                sol = (((x3-x2 *b) // x1), b)
    if sol != (-1,-1):
        fewest += 3 * sol[0] + sol[1]



print(fewest)