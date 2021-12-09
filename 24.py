# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def getLPRecursive(input, output="", result=[]): # Expects ordered array of n digits
    # Annoying verbosity
    # l = len(result)
    # if (l % 100000 == 0):
    #     print(f"len(result) = {l}")
    #     if (l >= 1000000):
    #         print(f"1000000th permutation is: {result[999999]}")
    #         exit(0)

    # Main loop
    for i in input: # [0,1,2]
        digitBank = input.copy()
        # newOutput = output.copy() # TODO: Can this be removed?
        newOutput = output
        
        # TODO: Can this be moved outside the loop?
        if (len(input) == 1): # Then final iteration
            # newOutput.append(i)
            newOutput += str(i)
            result.append(newOutput)
            break

        # newOutput.append(i) # Potential outputs for 1st iteration = [0,x,x]
        newOutput += str(i)
        digitBank.remove(i) # [0,1,2] --> [1,2]

        getLPRecursive(digitBank, newOutput, result)
    return result

def getLPStatic(input): # Expects ordered array of 3 digits
    result = []
    for i in input: # [0,1,2]
        iDigitBank = input.copy()

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
    # result = getLPRecursive([0,1,2], [], "")
    # result = getLPRecursive([], "", [0,1,2])
    result = getLPRecursive([0,1,2])
    print(result)

    # result = getLPRecursive([], 0, "", [0,1,2,3,4,5,6,7,8,9])
    # print(result[999999])

if __name__ == "__main__":
    main()


# Small note:
# The first half of the output array will contain the inverse of the second half
# (unordered, unforunately) 