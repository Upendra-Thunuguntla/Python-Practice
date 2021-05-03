#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    sums = []
    ret = []
    for i in range (0, len(sticks)-2):
        if (sticks[i]+sticks[i+1]>sticks[i+2]):
            sums.append(sticks[i]+sticks[i+1]+sticks[i+2])
            ret.append(str(sticks[i])+' '+str(sticks[i+1])+' '+str(sticks[i+2]))
            # ret.append(sticks[i]+sticks[i+1]+sticks[i+2])
    if len(sums) == 0:
        return ('-1') 
    return (ret[sums.index(max(sums))])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    fptr.write(result)
    fptr.write('\n')
