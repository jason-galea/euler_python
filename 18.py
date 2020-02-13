#!/usr/bin/env python3
from functions import *

tri = [
    [75]
    , [95, 64]
    , [17, 47, 82]
    , [18, 35, 87, 10]
    # , [20, 4, 82, 47, 65]
    # , [19, 1, 23, 75, 3, 34]
    # , [88, 2, 77, 73, 7, 63, 67]
    # , [99, 65, 4, 28, 6, 16, 70, 92]
    # , [41, 41, 26, 56, 83, 40, 80, 70, 33]
    # , [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
    # , [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
    # , [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
    # , [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
    # , [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
    # , [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

result = 0

# Print every permutation in strings of binary, where 0 = left and 1 = right
    # The permutations at a given row equal 2**(len(row))
# Permutations need to be a string of length (len(tri) - 1), eg "0101" for 5 levels
# https://stackoverflow.com/questions/699866/python-int-to-binary-string

# For now...
# permutation = "0101"

# For each permutation, interpret each character as a path. Calculate path values
for i in range(2**(len(tri) - 1)) :
    permutation = str(bin(i))[2:]

    # Adding leading zero characters
    while len(permutation) < len(tri) - 1:
        permutation = '0'.join(permutation)

    print(permutation)
    
    # current_row = 0
    # current_pos = 0
    # value = tri[current_row][current_pos]

    # print(value)

    # for choice in permutation:
    #     current_row += 1
    #     if choice == "0":
    #         value += tri[current_row][current_pos]
    #     else:   # Choice == 1
    #         current_pos += 1
    #         value += tri[current_row][current_pos]

    #     print(tri[current_row][current_pos])





# If value is greater than 'result', result = value

# Print result