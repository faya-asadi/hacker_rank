#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jump = 0;
    index = 0
    while index < len(c)-2 :
        if  c[index+2] == 0:
            index = index+2
           
        elif c[index] == 0:
            index = index+1
        jump += 1  
    return jump+1 if index < len(c)-1  else jump   
  


result = jumpingOnClouds([0,0,1,0,0,1,0])
print(result)

    