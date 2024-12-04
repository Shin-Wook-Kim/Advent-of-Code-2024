
result = 0


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day3/Day3Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            s_line = line.split('mul(')
            if len(s_line) > 1:
                for sen in s_line:
                    s_sen = sen.split(',')
                    if len(s_sen) > 1:
                        arg1 = s_sen[0]
                        if arg1.isdigit():
                            s_sen2 = s_sen[1]
                            if ')' in s_sen2:
                                arg2 = s_sen2.split(')')[0]
                                if arg2.isdigit():
                                    res = int(arg1) * int(arg2)
                                    result += res


print(result)
