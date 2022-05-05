#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
from collections import Counter

def makeAnagram(a, b):
    # Write your code here
    counter = 0
    big = Counter(a) if len(a) > len(b) else Counter(b)
    small = Counter(a) if len(a) <= len(b) else Counter(b)
    
    diff = big-small
    counter += sum(diff.values())   
    
    diff = small-big
    counter += sum(diff.values())    
    
    return counter 

    
if __name__ == '__main__':
   
    a = "fcrxzwscanmligyxyvym"
    b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
   

    res = makeAnagram(a, b)
    print(res)

    
