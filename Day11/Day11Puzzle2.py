import math


stones = []



with open("c:/Users/Shin/Documents/Advent-of-Code-2024/Day11/Day11Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            s_line = line.split()
            for word in s_line:
                stones.append(int(word))





def change(line):
    res = []
    for stone in line:
        if stone == 0:
            res.append(1)
        else:
            l = math.floor(math.log10(stone)) + 1
            if l % 2 == 0:
                a = stone //(10**(l//2))
                b = stone - a*(10**(l//2))
                res.append(a)
                res.append(b)
            else:
                res.append(stone * 2024)
    return res


def change_r(stone, num, k):
    if num == k:
        return 1
    if stone == 0:
        return change_r(1,num+1,k)
    l = math.floor(math.log10(stone)) + 1
    if l % 2 == 0:
        return change_r(stone // (10**(l//2)),num+1,k) + change_r(stone % (10**(l//2)),num+1,k) 
    return change_r(stone*2024,num+1,k)


c_1 = [[] for i in range(10)]
c_2 = [[] for i in range(10)]

for i in range(10):
    for j in range(10):
        c_1[i].append(change_r(i,10-j,10))

for i in range(10):
    res = [i]
    for j in range(10):
        res = change(res)
    c_2[i] = res


def change_rm(stone,num,k):
    if num == k:
        return 1
    if (stone < 10):
        if (num > k-10):
            return c_1[stone][k-num]
        else:
            l = 0
            for s in c_2[stone]:
                l += change_rm(s,num+10,k)
            return l
    if stone == 0:
        return change_rm(1,num+1,k)
    l = math.floor(math.log10(stone)) + 1
    if l % 2 == 0:
        return change_rm(stone // (10**(l//2)),num+1,k) + change_rm(stone % (10**(l//2)),num+1,k) 
    return change_rm(stone*2024,num+1,k)





#l = 0

#for stone in stones:
#    l += change_rm(stone,0,50)

#print(l)






c_3 = [[] for i in range(25)]

for i in range(25):
    for j in range(25):
        c_3[i].append(change_r(i,25-j,25))


def change_rm2(stone,num,k):
    if num == k:
        return 1
    if (stone < 25) and (num > k-25):
        return c_3[stone][k-num]
    if stone == 0:
        return change_rm2(1,num+1,k)
    l = math.floor(math.log10(stone)) + 1
    if l % 2 == 0:
        return change_rm2(stone // (10**(l//2)),num+1,k) + change_rm2(stone % (10**(l//2)),num+1,k) 
    return change_rm2(stone*2024,num+1,k)





#l = 0
#
#for stone in stones:
#    l += change_rm2(stone,0,65)
#
#print(l)
#
#got 3703014612940 after 4 minutes and 22 seconds




c_4 = [[] for i in range(100)]

for i in range(100):
    for j in range(25):
        c_4[i].append(change_r(i,25-j,25))





def change_rm3(stone,num,k):
    if num == k:
        return 1
    if (stone < 100) and (num > k-25):
        return c_4[stone][k-num]
    if stone == 0:
        return change_rm3(1,num+1,k)
    l = math.floor(math.log10(stone)) + 1
    if l % 2 == 0:
        return change_rm3(stone // (10**(l//2)),num+1,k) + change_rm3(stone % (10**(l//2)),num+1,k) 
    return change_rm3(stone*2024,num+1,k)


#l = 0
#
#for stone in stones:
#    l += change_rm3(stone,0,65)
#
#print(l)






c_5 = [[] for i in range(100)]

for i in range(100):
    for j in range(25):
        c_5[i].append(c_4[i][j])
    for j in range(25):
        c_5[i].append(change_rm3(i,25-j,50))



print('cache set up')

def change_rm4(stone,num,k):
    if num == k:
        return 1
    if (stone < 100) and (num > k-50):
        return c_5[stone][k-num]
    if stone == 0:
        return change_rm4(1,num+1,k)
    l = math.floor(math.log10(stone)) + 1
    if l % 2 == 0:
        return change_rm4(stone // (10**(l//2)),num+1,k) + change_rm4(stone % (10**(l//2)),num+1,k) 
    return change_rm4(stone*2024,num+1,k)


l = 0

for stone in stones:
    l += change_rm4(stone,0,75)

print(l)

