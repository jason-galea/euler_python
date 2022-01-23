from sympy import isprime

def yieldModRange(limit): # Yields 1, -1, 2, -2, etc. --> limit
    invert = False
    i = 1
    while i < limit:
        if invert:
            yield -i
            i += 1
        else:
            yield i
        invert = not invert
 
def evaluate(a, b): # Returns int of consecutive primes from formula n^2 + an + b
    result = 0
    n = 1
    while True:
        if isprime(abs((n * n) + (a * n) + b)): # is
            result += 1
        else:
            break
        n += 1

    return result

def main():
    RANGE = 1000
    resultDict = {
        "highest": 0
        , "a": 0
        , "b": 0
    }

    for a in yieldModRange(RANGE): # Generate range |a| < 1000 and |b| <= 1000, starting from |1|
        for b in yieldModRange(RANGE + 1):
            result = evaluate(a, b)
            if result > resultDict["highest"]:
                print("New highest number of consecutive primes found {0}, with cooefficients: {1}, {2}".format(
                    result, a, b
                ))
                resultDict = {"highest":result, "a":a, "b":b}

    print("Result is {0} * {1} = {2}".format(
        resultDict["a"], resultDict["b"], resultDict["a"] * resultDict["b"]
    ))
    exit(0)

if __name__ == "__main__":
    main()
