#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    unique=list(set(arr))
    unique.sort
    maximum = 0
    maxtype=arr[0]
    for typ in unique:
        if arr.count(typ)> maximum:
            maximum = arr.count(typ)
            maxtype = typ
    return maxtype
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
