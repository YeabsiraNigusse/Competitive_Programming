#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
   end = arr[n-1]
   for i in range(0,n):
      if arr[n-2-i] > end and n-2-i >=0:
         arr[n-1-i] = arr[n-2-i]
         for i in arr:
                print(f"{i}",end=" ")
         print("\r")
        
      else:
        arr[n-1-i] = end
        for i in arr:
                print(f"{i}",end=" ")
        print("\r")
        break
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

