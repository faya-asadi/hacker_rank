#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    v_count = 0
    in_vallay = False
    step_monitor = 0
    
    for stp in path:
        if stp == 'D':
            if step_monitor == 0:
                in_vallay = True 
            step_monitor -= 1
        elif stp== 'U':
            step_monitor += 1    
        if  in_vallay and step_monitor == 0: 
            v_count+=1
            in_vallay = False
            
    return v_count        


result = countingValleys(8, "UDDDUDUU")
print(result)

   