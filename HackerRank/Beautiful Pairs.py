#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    n = len(A)
    X=[]
    for i in A[::-1]:
        if i in B:
            A.remove(i)
            B.remove(i)
            X.append(i)
    return n-1 if len(X)==n else len(X)+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
