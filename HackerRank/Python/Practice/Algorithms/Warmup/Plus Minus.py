#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive=0
    negative=0
    zero=0
    for val in arr:
        
        if val < 0:
            negative+=1
        elif val>0:
            positive+=1
        else:
            zero+=1
    arlen=len(arr)
    print('%.6f' % (positive/arlen))
    print('%.6f' % (negative/arlen))
    print('%.6f' % (zero/arlen))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
