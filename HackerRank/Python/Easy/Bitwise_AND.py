#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#
def isValid(num,K):
    bin_number='0b0'+bin(num)[2:]
    nxt=bin_number[::-1].replace('0','1',1)[::-1]
    if int(nxt,2)<=K:
        return True
    return False
def bitwiseAnd(N, K):
    for i in range(K-1,-1,-1):
        if  isValid(i,N):
            return i  
    return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
