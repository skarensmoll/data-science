#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def getMedian(arr):
    numItems = len(arr)
    if ((numItems % 2) == 0) :
        middleIndex = int(numItems / 2)
        median = (arr[middleIndex - 1] + arr[middleIndex]) / 2
        result = { 'median': int(median), 'index': middleIndex, 'exclude': False }
        return result
    else :
        middleIndex = int(math.floor(numItems/2))
        median = arr[middleIndex]
        result = { 'median': int(median), 'index': middleIndex, 'exclude': True }
        return result


        
def quartiles(arr):
    arr = sorted(arr)
    q1 = getMedian(arr)
    q2 = 0
    q3 = 0
    index = q1['index']
     
    if(q1['exclude']) :
        q2 = getMedian(arr[0:index])
        q3 = getMedian(arr[index + 1::])
    else:
        q2 = getMedian(arr[0:index])
        q3 = getMedian(arr[index::])
    
    return [ q2['median'], q1['median'], q3['median'] ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
