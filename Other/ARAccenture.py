inpS = input().split(" ")
inp = [int(x) for x in inpS]
l=[]
weight = 0
inp.sort()
while(True):
    l.append(inp.pop(0))
    if(sum(l)==sum(inp)):
        weight = sum(l)
        print(weight)
        break


    