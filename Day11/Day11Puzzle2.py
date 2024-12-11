stones = []



with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day11/Day11Input1.txt", 'r') as file:
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
        elif len(str(stone)) % 2 == 0:
            l = len(str(stone))//2
            a = int(str(stone)[:l])
            b = int(str(stone)[l:])
            res.append(a)
            res.append(b)
        else:
            res.append(stone * 2024)
    return res


stones = [0]

for i in range(75):
    print(i)
    stones = change(stones)

print(len(stones))

