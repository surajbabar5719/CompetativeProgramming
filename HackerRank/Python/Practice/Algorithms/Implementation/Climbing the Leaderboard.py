#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    # Write your code here
    output=[]
    i=0
    ranked=sorted(set(ranked))
    for point in player:
        try:
            while ranked[i] < point:
                i+=1
        except:
            ranked.append(point)
        if ranked[i] != point:
            ranked.insert(i,point)
        output.append(len(ranked)-i)      
    return output
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
