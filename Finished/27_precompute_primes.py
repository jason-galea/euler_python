
def yieldPrimes(i):		# Accepts int, yields all yieldPrimes below and including 'i'
	arr = [True] * (i + 1)
	for x in range(2,i + 1):
		if arr[x]:
			yield x
			for y in range(x,i + 1,x):
				arr[y] = False

def isPrime(n):
    if n==2 or n==3: return True # Check 2, 3
    if n%2==0 or n<2: return False # Check 4, 6, 8, all negative numbers
    if n<8: return True # Check 5, 7
    for x in range(3, int(pow(n, 0.5)) + 1, 2): # Only odd numbers > 2
        if n % x==0:
            return False
    return True

def main():
    RANGE = 1000
    noConsecutivePrimes = 0
    result = 0

    # Precompute primes for "b"
    # This takes advantage of the fact that prime coefficients
    # produce the most consecutive primes
    b_list = [i for i in range(2,RANGE+1) if isPrime(i)]
    # b_list = [i for i in yieldPrimes(RANGE + 1)]

    for a in range(-RANGE + 1,RANGE):
        for b in b_list:
            i = 0
            while isPrime(i**2 + a*i + b):
                i += 1
                if i > noConsecutivePrimes:
                    noConsecutivePrimes = i
                    result = a*b
                  
    print(result)

if __name__ == "__main__":
    main()
