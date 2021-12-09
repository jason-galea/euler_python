# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def getLPRecursive(outputArray, inputArray): # Expects ordered array of n digits
    result = []
    for i in inputArray: # [0,1,2]
        digitBank = inputArray.copy()
        newOutputArray = outputArray.copy()
        
        if (len(inputArray) == 1): # Then final iteration
            newOutputArray.append(i)
            return newOutputArray

        newOutputArray.append(i) # Potential outputs for 1st iteration = [0,x,x]
        digitBank.remove(i) # [0,1,2] --> [1,2]

        result.append(getLPRecursive(newOutputArray, digitBank)) # Recurse
        # 2nd iteration:    getLPRecursive([0], [1,2])
        # 3rd iteration:    getLPRecursive([0,1], [2])
    return result # Return once, after all recursion

def getLPStatic(inputArray): # Expects ordered array of 3 digits
    result = []
    for i in inputArray: # [0,1,2]
        iDigitBank = inputArray.copy()

        iOutput = []
        iOutput.append(i) # Potential outputs for this iteration = [0,x,x]
        iDigitBank.remove(i) # [0,1,2] --> [1,2]

        for j in iDigitBank: # [1,2]
            jDigitBank = iDigitBank.copy()

            jOutput = iOutput.copy()
            jOutput.append(j) # Potential outputs for this iteration = [0,1,x]
            jDigitBank.remove(j) # [1,2] --> [2]

            for k in jDigitBank: # [2]
                kDigitBank = jDigitBank.copy()

                kOutput = jOutput.copy()

                if (len(jDigitBank) == 1): # Redundant, illistrative
                    kOutput.append(k)
                    result.append(kOutput)

                # kOutput.append(k) # Potential outputs for this iteration = [0,1,2]
                # kDigitBank.remove(k) # [2] --> []



    return result

def main():
    # result = getLPStatic([0,1,2])
    result = getLPRecursive([], [0,1,2])
    print(result)

    # result = getLPRecursive([0,1,2,3,4,5,6,7,8,9])
    # print(result[1000000])

if __name__ == "__main__":
    main()


# Small note:
# The first half of the output array will contain the inverse of the second half
# (unordered, unforunately) 