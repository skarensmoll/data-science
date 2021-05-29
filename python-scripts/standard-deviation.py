#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    
    sumArr = 0
    numItems = len(arr) 
    
    mean = sum(arr) / numItems

    std = math.sqrt(sum([((i-mean)**2) for i in arr])/numItems)
    print(format(std, ".1f") )
    
    # Print your answers to 1 decimal place within this function

if __name__ == '__main__':
    n = int(raw_input().strip())

    vals = map(int, raw_input().rstrip().split())

    stdDev(vals)
