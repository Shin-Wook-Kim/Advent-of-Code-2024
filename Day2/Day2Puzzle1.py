
reports = []


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day2/Day2Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            s_line = line.split()
            report = []
            for i in range(len(s_line)):
                report.append(int(s_line[i]))
            reports.append(report)
    

safe = 0

for i in range(len(reports)):
    report = reports[i]
    l = len(report)
    if l ==1:
        safe += 1
    else:
        type = True
        if (report[0] == report[1]):
            continue
        if (report[0] < report[1]):
            type = False
        j = 0
        while (j < len(report)-1):
            current = report[j]
            next = report[j+1]
            if type:
                if not (0 < current - next < 4):
                    break
            else:
                if not (-4 < current - next < 0):
                    break
            j += 1
        if j == len(report)-1:
            safe += 1
        
print(safe)




