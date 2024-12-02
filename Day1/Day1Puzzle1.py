left = []
right = []


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day1/Day1Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            s_line = line.split()
            left.append(int(s_line[0]))
            right.append(int(s_line[1]))


left.sort()
right.sort()

l = len(left)

dist = 0

for i in range(l):
    dist += abs(left[i]-right[i])

print(dist)