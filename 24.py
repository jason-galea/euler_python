#!/usr/bin/env python3


# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def getLPRecursive():
    pass

def getLPStatic(inputArray): # Expects ordered array of 3 digits
    result = []
    for i, iDigit in enumerate(inputArray):
        iArray = inputArray.copy() # Local duplicate of [0,1,2]
        iOutput = []
        iOutput.append(iArray.pop(i)) # Stem of new branch [0,?,?]

        for j, jDigit in enumerate(iOutput):
            jArray = iArray.copy() # Local duplicate of [1,2]
            jOutput = iOutput.copy()
            jOutput.append(jArray.pop(j)) # Stem of new branch [0,1,?]

            for k, kDigit in enumerate(jOutput):
                kArray = jArray.copy() # Local duplicate of [2]
                kOutput = jOutput.copy()
                kOutput.append(kArray.pop(k))
                
                result.append(kOutput)

    return result

def main():
    result = getLPStatic([0,1,2])
    # result = getLPRecursive([0,1,2,3,4,5,6,7,8,9])
    for s in result:
        print(s)

if __name__ == "__main__":
    main()


# Small note:
# The first half of the output array will contain the inverse of the second half
# (unordered, unforunately) 