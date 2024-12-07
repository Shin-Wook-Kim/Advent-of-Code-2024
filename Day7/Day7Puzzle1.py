
c_equations = []


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day7/Day7Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            temp = []
            s_line1 = line.split(sep=':')
            temp.append(int(s_line1[0]))
            s_line2 = s_line1[1].split()
            for char in s_line2:
                temp.append(int(char))
            c_equations.append(temp)


result = 0
l = 0



for equation in c_equations:
    l = len(equation)
    test = equation[0]
    temp = equation[1]
    if l == 2:
        if test == temp:
            result += test
    else:
        for i in range(2**(l-2)):
            temp = equation[1]
            for j in range(l-2):
                op = (i // (2 ** j)) % 2
                if op == 0:
                    temp = temp + equation[j+2]
                else:
                    temp = temp * equation[j+2]
            if test == temp:
                result += test
                break

print(result)