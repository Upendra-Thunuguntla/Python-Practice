#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPeople function below.
def maximumPeople(popu, townLocation, cloudLocation, cloudRange):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    # coverage = []
    totalPop = sum(popu)
    darkPop = 0
    maxCovered = max(cloudRange)
    maxPop = max(popu)
    # for i in range (len(cloudLocation)):
        # coverage.append([cloudLocation[i]-cloudRange[i],cloudLocation[i]+cloudRange[i]])
    # print(coverage[0][0])
    pops = []
    for x in range (0,len(cloudLocation)):
        cloudCove = 0
        for y in range (0, len(townLocation)):
            start = cloudLocation[x]-cloudRange[x]
            end  = cloudLocation[x]+cloudRange[x]
            if start <=townLocation[y] and townLocation[y]<= end:
                darkPop += popu[y]
                cloudCove += popu[y]
        pops.append(cloudCove)

    
    print(darkPop)


    return totalPop-(darkPop-max(pops))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
