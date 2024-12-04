
word_search = []


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day4/Day4Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            l = len(line)
            row = []
            for i in range(l):
                char = line[i]
                if not(char == '\n'):
                    row.append(line[i])
            word_search.append(row)

number = 0

nrow = len(word_search)
ncol = len(word_search[0])

def DoubleMAS(char1,char2,char3,char4,char5):
    if (char1 == 'M') and (char2 == 'A') and (char3 == 'S') and (char4 == 'M') and (char5 == 'S'):
        return True
    if (char1 == 'M') and (char2 == 'A') and (char3 == 'S') and (char4 == 'S') and (char5 == 'M'):
        return True
    if (char1 == 'S') and (char2 == 'A') and (char3 == 'M') and (char4 == 'S') and (char5 == 'M'):
        return True
    if (char1 == 'S') and (char2 == 'A') and (char3 == 'M') and (char4 == 'M') and (char5 == 'S'):
        return True
    return False

            




for i in range(nrow):
    for j in range(ncol):
        if (j+2 < ncol) and (i+2 < nrow):
            number += int(DoubleMAS(word_search[i][j],word_search[i+1][j+1],word_search[i+2][j+2],word_search[i][j+2],word_search[i+2][j]))

print(number)
            