#!/bin/python3
#https://www.hackerrank.com/challenges/angry-children/problem
import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    reses = []
    for i in range (0,len(arr)-k+1):
        print(arr[k+i-1],arr[i])
        reses.append(arr[k-1+i]-arr[i])
    return min(reses)


    
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
