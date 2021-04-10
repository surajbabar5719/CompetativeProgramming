#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    all_sum = sum(arr)
    minimum = all_sum - max(arr)
    maximum = all_sum - min(arr)
    print(minimum, maximum)
        
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
