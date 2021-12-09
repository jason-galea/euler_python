
def getLPRecursive(input, limit, output="", result=[], resultLength=0):
    if (resultLength == limit):
        print(f"Permutation #{limit} is: {result[limit - 1]}")
        exit(0)

    if (len(input) == 1): # If final node of branch, save output
        result.append(output + str(input[0]))
        return resultLength + 1

    for i in input: # Eg: [0,1,2]
        digitBank = input.copy()
        newOutput = output + str(i) # Potential outputs for 1st iteration = '0xx'
        digitBank.remove(i) # [0,1,2] --> [1,2]

        resultLength = getLPRecursive(digitBank, limit, newOutput, result, resultLength) # Recurse
    
    return resultLength

getLPRecursive([0,1,2,3,4,5,6,7,8,9], 1000000)
