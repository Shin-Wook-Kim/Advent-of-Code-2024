
dampened_reports = []


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day2/Day2Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            s_line = line.split()
            dampened_report = []
            for i in range(len(s_line)):
                dampened = []
                for j in range(len(s_line)):
                    if not(i == j):
                        dampened.append(int(s_line[j]))
                dampened_report.append(dampened)
            dampened_reports.append(dampened_report)




safe = 0


def check_safe(report):
    check = False   
    l = len(report)
    if l ==1:
        check = True
    else:
        type = True
        if (report[0] == report[1]):
            return check
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
            check = True
    return check





for i in range(len(dampened_reports)):
    dampened_report = dampened_reports[i]
    d = len(dampened_report)
    j = 0
    c_safe = False
    while ( (c_safe == False) and (j < d)):
        c_safe = check_safe(dampened_report[j])
        j += 1
    if c_safe == True:
        safe += 1
    
    
    

    
print(safe)





    
