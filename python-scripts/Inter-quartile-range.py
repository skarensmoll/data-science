#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
# Lower half (L): 6, 6, 6, 6, 6, 8, 8, 8, 10, 10
# Upper half (U): 12, 12, 12, 12, 16, 16, 16, 16, 16, 20
#
# INPUTS
#    6

#    6 12 8 10 20 16

#    5 4 3 2 1 5
#
# OUTPUTS
# 9.0
# Q3 - Q1

def getSArray(values, freqs):
    s = []
    for i in range(len(values)):
        s += [values[i]] * freqs[i] 
        
    s = sorted(s)
    return s

def getMiddleIndexMedian(arr):
    lenghtS = len(arr)
    
    if(lenghtS % 2 == 0) :
        middleIndex = int(lenghtS / 2)
        median = (arr[middleIndex] + arr[middleIndex -1]) / 2
        result = { 'midIndex' : middleIndex, 'exclude': False, 'median': median }    
    else :
        middleIndex =  int(math.floor(lenghtS / 2))
        median = arr[middleIndex]
        result = { 'midIndex' : middleIndex, 'exclude': True, 'median': median }    

    return result

def interQuartile(values, freqs):
    s = getSArray(values, freqs)
    lenghtS = len(s)
    q2 = getMiddleIndexMedian(s)
    
    
    if q2['exclude'] :
        lowerHalf = s[0:q2['midIndex']]
        upperHalf = s[(q2['midIndex'] + 1)::]
    else :
        lowerHalf = s[0:(q2['midIndex'])]
        upperHalf = s[q2['midIndex']::]
     
    q1 = getMiddleIndexMedian(lowerHalf)
    q3 = getMiddleIndexMedian(upperHalf)
    interQuartileResult = q3['median'] - q1['median']
    
    print(format(interQuartileResult, ".1f"))
    
        

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
