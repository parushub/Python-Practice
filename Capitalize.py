#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    cap_next = True
    res=""
    for ch in s:
        if(ch==" "):
            res+=ch
            cap_next=True
        elif (cap_next):
            res+=ch.upper()
            cap_next=False
        else:
            res+=ch
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
