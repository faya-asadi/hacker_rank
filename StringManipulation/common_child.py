#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
   l = len(s1)+1
   # other ways to create 2d array like: arr = [[0] * l] * l  are problematic, the copy gets manipulated wrongly 
   arr = [[0 for i in range(l)] for j in range(l)]
   
   for i in range(1, l):
    for j in range(1, l):
        if s1[i-1] == s2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][ j], arr[i][ j-1])
   return max(max(arr))    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s1 = input()

    # s2 = input()
    
    


    result = commonChild("HARRY", "SALLY")
    print(result)
    
    
    result = commonChild("SHINCHAN", "NOHARAAA")
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
