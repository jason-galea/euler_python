from functools import cache

@cache
def isPrime(n):
    if n==2 or n==3: return True # Check 2, 3
    if n%2==0 or n<2: return False # Check 4, 6, 8, all negative numbers
    if n<8: return True # Check 5, 7
    for x in range(3, int(pow(n, 0.5)) + 1, 2): # Only odd numbers > 2
        if n % x==0:
            return False
    return True
 
def evaluate(a, b): # Returns int of consecutive primes from formula n^2 + an + b
    result = 0
    n = 1
    while True:
        if isPrime(abs((n * n) + (a * n) + b)):
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

    for a in range(-RANGE + 1, RANGE): # -999 --> 999
        for b in range(-RANGE, RANGE + 1): # -1000 --> 1000
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
