

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
                temp.append(int(s_line[1][2:-1]))
                temp.append(int(s_line[2][2:]))




fewest = 0

for machine in machines:
    x1 = machine[0]
    y1 = machine[1]
    x2 = machine[2]
    y2 = machine[3]
    x3 = machine[4]
    y3 = machine[5]
    sols = []
    for i in range(101):
        for j in range(101):
            if (x1 * i + x2 * j == x3) and (y1 * i + y2 * j == y3):
                sols.append((i,j))
    if not(sols == []):
        temp = 400
        for sol in sols:
            res = 3*sol[0] + sol[1]
            if res < temp:
                temp = res
        fewest += temp


print(machines[-1])

print(fewest)