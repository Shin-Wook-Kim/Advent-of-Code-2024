
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

def XMAS(char1,char2,char3,char4):
    if (char1 == 'X') and (char2 == 'M') and (char3 == 'A') and (char4 == 'S'):
        return True
    if (char1 == 'S') and (char2 == 'A') and (char3 == 'M') and (char4 == 'X'):
        return True
    return False

            




for i in range(nrow):
    for j in range(ncol):
        if j+3 < ncol:
            number += int(XMAS(word_search[i][j],word_search[i][j+1],word_search[i][j+2],word_search[i][j+3]))
        if i+3 < nrow:
            number += int(XMAS(word_search[i][j],word_search[i+1][j],word_search[i+2][j],word_search[i+3][j]))
        if (j+3 < ncol) and (i+3 < nrow):
            number += int(XMAS(word_search[i][j],word_search[i+1][j+1],word_search[i+2][j+2],word_search[i+3][j+3]))
        if (j > 2) and (i+3 < nrow):
            number += int(XMAS(word_search[i][j],word_search[i+1][j-1],word_search[i+2][j-2],word_search[i+3][j-3]))

print(number)
            