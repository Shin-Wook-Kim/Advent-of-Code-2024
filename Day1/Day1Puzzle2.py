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

l = len(left)

similarity_score = 0

left.sort()
right.sort()

temp = 0

for i in range(l):
    if (i > 0) and (left[i-1] == left[i]):
        similarity_score += temp
    else:
        temp = 0
        left_value = left[i]
        for j in range(l):
            if left_value == right[j]:
                temp += left_value
            if left_value < right[j]:
                break
        similarity_score += temp

print(similarity_score)