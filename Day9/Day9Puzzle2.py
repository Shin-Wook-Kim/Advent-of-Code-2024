
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


fileblocks = []

for i in range(l):
    dl = int(disk_map[i])
    if i % 2 == 0:
        for j in range(dl):
            fileblocks.append(i//2)
    else:
        for j in range(dl):
            fileblocks.append('.')


#fileblocks = [0,0,'.','.','.',1,1,1,'.','.','.',2,'.','.','.',3,3,3,'.',4,4,'.',5,5,5,5,'.',6,6,6,6,'.',7,7,7,'.',8,8,8,8,9,9]


l = len(fileblocks)
print(l)

temp = 0
j = 1
count = 0
init = 0
init_j = 0
len = 0
len_j = 0

while(j < l+1):
    print(j)
    found = False
    while((not found) and (j < l+1)):
        if fileblocks[-j] == '.':
            j += 1
        else:
            found = True
            temp = fileblocks[-j]
            init_j = j
            while((fileblocks[-j] == temp)):
                if j < l:
                    j += 1
                else:
                    j += 1
                    break
            len_j = j - init_j
    if found:
        i = 0
        while(i + j < l+1):
            if fileblocks[i] == '.':
                init = i
                while ((fileblocks[i] == '.') and (i+j < l+1)):
                    i += 1
                len = i - init
                if (len_j < len + 1):
                    for k in range(len_j):
                        fileblocks[0-init_j-k] = '.'
                        fileblocks[init+k] = temp
                    break
            else:
                i += 1



checksum = 0

i = 0


while(i < l):
    if fileblocks[i] == '.':
        i += 1
    else:
        checksum += i * fileblocks[i]
        i += 1




print(checksum)




