l = list(map(int,input().split()))
if sum(l)%2==0:
    print(sum(l)//2)
else:
    print((sum(l)-1)//2)


    