DEBUG = False

def is_a_factor(potential_factor, i):
    return (i % potential_factor == 0)

def sqrt(i):
	return i**0.5
	
def is_prime(i):
	for x in range(2, int(sqrt(i)) + 1):
		# if (i % x == 0):
		if (is_a_factor(x, i)):
			return False

	return True

def yield_primes(i):	### Accepts int, yields all primes below and including 'i'
	arr = [True] * (i + 1)
	for x in range(2,i + 1):
		if arr[x]:
			yield x

			for y in range(x,i + 1,x):
				arr[y] = False

def is_coprime(a, b): ### Assumes a < b

    ### If ANY common factors, return False
    ### NOTE: "i" ONLY fails when i is prime
    ### NOTE: So there's no point checking for non-prime factors

    for i in range(2, a + 1): ### Naive
    # for i in yield_primes(a): ### Very high overhead :/

    # ### Don't check range above sqrt(a) + 1
    # ### NOTE: This fails, because you can't skip values (why though...)
    # for i in range(2, int(sqrt(a)) + 1):

        # if (a % i == 0) and (b % i == 0):
        if (is_a_factor(i, a)) and (is_a_factor(i, b)):
            # print(f"is_coprime({a}, {b}) == False")
            # print(f"{i} IS a factor of {a} and {b}")
            return False

        # else:
        #     print(f"{i} IS NOT a factor of {a} and {b}")

    # print(f"is_coprime({a}, {b}) == True")
    return True

def totient(n, debug=DEBUG):

    relative_primes = {1}

    for i in range(2, n): ### Naive
        if (is_coprime(i, n)):
            relative_primes.add(i)

    if (debug): print(f"(n = {n}): relative_primes = {relative_primes}")

    return len(relative_primes)

def main(limit):
    ### Find N that produces highest n/φ(n)
    ### NOTE: AKA: N with most factors at lowest value

    ### TODO: Target N will never be prime
    ### DONE: Target N will never be odd

    result = 0
    max_n_on_tn = 0

    # for n in range(2, limit + 1): ### Naive
    # for n in range(2, limit + 1, 2):
    for n in range(10, limit + 1, 10): ### Breaks if (limit < 30)
        
        if (is_prime(n)): continue ### TODO
        # if (n % 3 != 0): continue ### This is very janky
        # if (not is_a_factor(3, n)): continue ### This is very janky
        
        current_n_on_tn = n/totient(n)
        if (current_n_on_tn > max_n_on_tn):
            result = n
            max_n_on_tn = current_n_on_tn

            print(f"(n = {n}): max_n_on_tn = {max_n_on_tn}")
            totient(n, debug=True)

    print(f"\nFor n ≤ {limit}, n/φ(n) produces a maximum at n = {result}")
    print(f"For n = {result}, n/φ(n) = {max_n_on_tn}")

if __name__ == "__main__":

    ### Best times!!!
    # main(10)        ### 0m00.013s
    # main(100)       ### 0m00.013s
    # main(500)       ### 0m00.018s
    # main(1000)      ### 0m00.053s
    main(5000)      ### 0m4.871s
    # main(10000)     ### 0m39.498s
    # main(50000)     ### 
    # main(100000)    ### 
    # main(500000)    ### 

    ### GOAL
    # main(1000000)   ### 
