#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write you
    i = 0
    len_s = len(s)
    len_t = len(t)
    print(9 % -2)
    min_l_s=min((len_s,len_t))
    while i<min_l_s and t[i] == s[i]:
        i+=1
    if len_t + len_s <= k:
        return 'Yes'
    if (k - len_s - len_t + 2*i) >=0 and (k - len_s - len_t + 2*i) % 2 == 0:
        return 'Yes'
    return 'No'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
