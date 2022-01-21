
def yieldModRange(l): # Yields |i| --> limit, starting from |1|
    invert = False
    i = 1
    while i < l:
        if invert:
            yield -i
            i += 1
        else:
            yield i
        invert = not invert

def sqrt(i):
	return i**(1/2)
	
def is_prime(i):
	for x in range(2, int(sqrt(i)) + 1):
		if i % x == 0:
			return False
	return True
 
def evaluate(a, b): # Returns number of consecutive primes generated by formula n^2 + an + b
    result = 0
    n = 1
    while True:
        if is_prime(abs((n * n) + (a * n) + b)):
            result += 1
        else:
            # print("Found {0} consecutive primes, with cooefficients {0} and {b}".format(
            #     result, a, b
            # ))
            break
        n += 1

    # print("Found {0} consecutive primes, with cooefficients {1} and {2}".format(
    #     result, a, b
    # ))
    return result # Returns int for number of consecutive primes

def main():
    LIMIT = 1000
    resultDict = {
        "highestConsecutivePrimes": 0
        , "a": 0
        , "b": 0
    }

    for a in yieldModRange(LIMIT): # Generate range |a| < 1000 and |b| <= 1000, starting from |1|
        for b in yieldModRange(LIMIT + 1):
            result = evaluate(a, b)
            if result > resultDict["highestConsecutivePrimes"]:
                print("New highest number of consecutive primes found {0}, with cooefficients: {1}, {2}".format(
                    result, a, b
                ))
                resultDict["highestConsecutivePrimes"] = result
                resultDict["a"] = a
                resultDict["b"] = b

            # print(f"a = {a}, b = {b}")
        # print(f"a = {a}")

    # print("Highest number of consecutive primes found was {0}, with cooefficients: {1}, {2}".format(
    #     resultDict['highestConsecutivePrimes'], resultDict['a'], resultDict['b']
    # ))
    print(f"Result = a * b = {a} * {b} = {a * b}")
    exit(0)

if __name__ == "__main__":
    main()
