#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    match = {}
    count = 0
    for s in ar:
        if s in match:
            count+=1
            del match[s]
        else:
            match[s] = s
            
            
    return count


result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
print(result)