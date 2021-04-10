#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    length = range(s,t+1)
    total = 0
    for apple in apples:
        if a + apple in length:
            total += 1
    print(total)
    total = 0
    for orange in oranges:
        if b + orange in length:
            total += 1
    print(total)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
