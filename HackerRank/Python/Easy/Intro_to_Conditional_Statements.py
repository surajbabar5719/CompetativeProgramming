#!/bin/python3

import math
import os
import random
import re
import sys


def weird(N):
    if N%2==1:
        return 'Weird'
    if N in range(6,21):
        return 'Weird'
    return 'Not Weird'
if __name__ == '__main__':
    N = int(input())
    print(weird(N))
