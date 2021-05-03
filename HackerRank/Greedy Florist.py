#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if (k==len(c)):
        return sum(c)
    c.sort(reverse=True)

    print(c)
    pur = {}
    res = 0
    for i in range (0,k):
        pur['P'+str(i)] = 1
        res+= c[i]
    rem = c[k:]
    
    get = 0
    for j in range (0,len(rem)):
        res+=(pur['P'+str(get)] + 1) * rem[j]    
        pur['P'+str(get)] += 1 
        get +=1
        if (get>=k):
            get=0
    print(pur)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
