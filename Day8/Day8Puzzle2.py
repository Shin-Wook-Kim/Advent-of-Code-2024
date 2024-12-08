
n_row = 0
n_col = 0

ants = {}


with open("c:/Users/corpt/Documents/Advent-of-Code-2024/Day8/Day8Input1.txt", 'r') as file:
    file.seek(0)
    done = False
    i = 0
    j = 0
    while (not done):
        line = file.readline()
        if line == '':
            done = True
        else:
            for char in line:
                if char == '.':
                    j += 1
                elif char == '\n':
                    if i == 0:
                        n_col = j
                    else:
                        if not (j == n_col):
                            print('error : not a grid')
                    i += 1
                    j = 0
                else:
                    if char in ants:
                        ants[char].append((i,j))
                    else:
                        ants[char] = [(i,j)]
                    j += 1
    n_row = i+1

nodes = []
l=0


for ant in list(ants):
   locs = ants[ant]
   l = len(locs)
   for i in range(l):
       for j in range(l):
           if i == j:
               continue
           else:
               k = -49
               while k < 50:
                   node = ((k+1)*locs[i][0] - k*locs[j][0], (k+1)*locs[i][1] - k * locs[j][1])
                   k += 1
                   if (node[0] > -1) and (node[0] < n_row) and (node[1] > -1) and (node[1] < n_col):
                       if node in nodes:
                           continue
                       else:
                           nodes.append(node)


print(len(nodes))

