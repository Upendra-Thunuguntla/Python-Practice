import math
mod = 10**9 + 7 

def cntways(array):
    if len(array) <= 2:
        return 1
    left = [v for v in array if v < array[0]]
    right = [v for v in array if v > array[0]]
    return math.comb(len(left) + len(right), len(right))*cntways(left)*cntways(right)
        
print((cntways(list(map(int,input().split()))) - 1)%mod)



