import math

inp = 703
cols = []

for i in range (ord('A'),ord('Z')+1):
    cols.append(chr(i))

for i in range (ord('A'),ord('Z')+1):
    for j in range (ord('A'),ord('Z')+1):
        cols.append(chr(i)+chr(j))

colSize = len(cols)
print(str(math.ceil(inp/colSize))+cols[(inp%colSize)-1])

