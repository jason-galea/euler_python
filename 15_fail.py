#!/usr/bin/env python3
from functions import *

def paths(i):
    # if i != 1:
    # arr = [0] * (int(sqr(i)))
    # print(arr)
    # for x in range(0, len(arr) - 1): # Adds one in binary per cycle
    #     if arr[x] == 0:
    #         arr[x] += 1
    #     else:
    #         arr[x] = 0
    #         arr[x + 1] += 1
    #     print(arr)
    # print()

    for x in range(i**3):
        s = str(bin(x))[2:]
        # if len(s):
        print("Length: ", len(s), "Value: ", s)
            # print("Value: ", s)
        


size = int(input("\nEnter a number:\n"))
result = 0

# 1 = right, 0 = down

# write "paths()", that yields strings

# for each item in that function, check if it contains exactly "size"
# number of both 1's and 0's
# If it does, result += 1

# for x in paths(size):
#     print(x)

# print('"%s"' %(paths(size)))
paths(2)