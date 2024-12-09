
disk_map = ''

with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day9/Day9Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            disk_map = line


l = len(disk_map)

print(l)

fileblocks = []

for i in range(l):
    dl = int(disk_map[i])
    if i % 2 == 0:
        for j in range(dl):
            fileblocks.append(i//2)
    else:
        for j in range(dl):
            fileblocks.append('.')





l = len(fileblocks)


temp = 0
j = 1

for i in range(l):
    if i % 1000 == 0:
        print(i)
    if fileblocks[i] == '.':
        found = False
        while(not found):
            if (i+j) == l:
                break
            else:
                if fileblocks[-j] == '.':
                    j += 1
                else:
                    found = True
                    temp = fileblocks[-j]
                    fileblocks[i] = temp
                    fileblocks[-j] = '.'
        if not found:
            break



checksum = 0

i = 0


while(not (fileblocks[i] == '.')):
    checksum += i * fileblocks[i]
    i += 1




print(checksum)




