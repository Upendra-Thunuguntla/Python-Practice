def lexigrpohicallySmallArray(arr):
    
    compare = sorted(arr)
    mod = 1000000007 #Nine Zeros
    flag = False
    returnSum = 0
    for i in arr :
        if (i%2!=0):
            flag = True
            break

    if (flag):
        for i in range (0,len(arr)):
            returnSum+=(i+1)*compare[i]
    else:
        for i in range (0,len(arr)):
            returnSum+=(i+1)*arr[i]
    return returnSum%mod

print(lexigrpohicallySmallArray([4,2,5,6,3,2,1]))