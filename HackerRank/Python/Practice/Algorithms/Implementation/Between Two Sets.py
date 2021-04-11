#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
    # Write your code here
    minimum=max(a)
    maximum=min(b)
    count = 0
    for i in range(minimum,maximum+1,minimum):
        brk=False
        for val in a:
            if i % val != 0:
                brk = True
                break
        for val in b:
            if val % i !=0:
                brk = True
                break
        if not brk:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
