def ok(n):
    even =0
    odd = 0
    s = str(n); 
    for x in set(s):
        if (int(x)%2==0):
            even+=1
        else:
            odd+=1
    return all(s.count(d) == int(d) for d in set(s)) and (even == odd)
    

def solve(limit): 
    limit+=1
    while (True): 
        if (ok(limit)): 
            return limit
        limit+=1

def getList(n):
    return [m for m in range(1, n+1) if ok(m)]

nums = []
T = int(input())
for _ in range(T):
    N = int(input())
    nums.append(N)

res = getList(solve(max(nums)))
res.sort()

for x in range (len(nums)):
    for y in range (len(res)):
        if (nums[x] < res[y]):
            print(res[y])
            break





# 18
# 96
# 634
# 248
# 808
# 72
# 867
# 890
# 515
# 68
# 252
# 888
# 578
# 746
# 295
# 884
# 198
# 655
# 503