# from functools import cache

def yield_primes(i):    ### Accepts int, yields all primes below and including 'i'
    arr = [True] * (i + 1)

    for x in range(2, i + 1):
        if arr[x]:
            yield x

            for y in range(x, i + 1, x):
                arr[y] = False

def is_coprime_old(a, b): ### If ANY common factors, return False (Assumes a < b)
    # print(f"==> \tis_coprime({a}, {b})")
    # print(f"==> \t Are {a} & {b} coprime?")

    ### Early exits
    if (abs(a - b) == 1): return True ### Consecutive numbers are always coprime
    if (b % a == 0): return False ### Account for not including 'a' as a factor of itself below

    sqrt_a = a**0.5 ### Could be a float

    ### Find & check factors of 'a'
    for i in range(2, int(sqrt_a + 1)):
        # print(f"==> \t\t Is {i} a factor?")

        if (a % i == 0):
            # print(f"==> \t\t\t {i} is a factor of {a}")

            if (b % i == 0):
                # print(f"==> \t\t\t {a} & {b} are not coprime (common factor {i})")
                return False

            if (i != sqrt_a) and (b % (int(a/i)) == 0): ### Check matching factor if not square root
                # print(f"==> \t\t\t {a} & {b} are not coprime (common factor {i})")
                return False
                    
    # print(f"==> \t\t\t {a} & {b} ARE coprime (No common factors found)")
    return True

def is_coprime_old_v2(i, factors_of_n, n=1): ### Returns True if 'i' is cleanly divisible by any factor in given set
    
    ### Early exits
    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    for factor in factors_of_n:
        if (i % factor == 0):
            return False

    return True

def is_coprime(i, n): ### Returns True if 'i' is cleanly divisible by any factor in given set
    
    ### Early exits
    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below


    for factor_of_i in DICT_OF_FACTORS[i]:
        if (factor_of_i in DICT_OF_FACTORS[n]):
            return False

    return True



def factors(i):        # Accepts int, yields all factors of 'i', including 1 and 'i'
    result = set()
    sqrt_i = i**0.5 ### Could be a float

    # for x in range(1, int(sqrt_i + 1)):
    for x in range(2, int(sqrt_i + 1)): ### Don't care about 1
        if (i % x == 0):

            result.add(x)

            if (x != sqrt_i): ### Only add matching factor if not square root
                result.add(int(i / x))

    return result


###################################################################
### "MAIN"
### Best times!!!
# LIMIT = 10         ### 0m00.013s           ### Answer = 6
# LIMIT = 50         ### 0m00.013s           ### Answer = 30
# LIMIT = 100        ### 0m00.013s           ### Answer = 30
# LIMIT = 500        ### 0m00.018s           ### Answer = 210
# LIMIT = 1000      ### 0m00.028s           ### Answer = 210
# LIMIT = 5000       ### 0m00.152            ### Answer = 2310
LIMIT = 10000      ### 0m00.661s           ### Answer = 2310
# LIMIT = 50000      ### 0m27.154s           ### Answer = 30030 (n/φ(n) = 5.2135)
# LIMIT = 100000     ### 2m30.528s           ### Answer = 30030
# LIMIT = 500000     ### 0m??.???s           ### Answer = ???

### GOAL
# LIMIT = 1000000    ### 0m??.???s           ### Answer = ???


### TODO: Compute a set of factors for each 'n'
### TODO: (Assuming you compute factors for ALL n < LIMIT, including odds), save factors to a dict as { n:set() }
### This would remove all computation from is_coprime(), allowing for ONLY lookups (of i and n)


"""
Find N that produces highest n/φ(n)
φ(n) is the count of numbers <= n, that are coprime with n

AKA, N with most factors and lowest value
"""

RESULT = 0
MAX_N_ON_TN = 0
DICT_OF_FACTORS = {}

####################################################################
### BEGIN MAIN LOOP (n)
for n in range(2, LIMIT + 1): ### "Naive", all numbers
# for n in range(2, LIMIT + 1, 2): ### Even numbers only (Target N will never be odd/prime)
# for n in range(10, LIMIT + 1, 10): ### Kind of cheating, incrementing based on previous answers
# for n in range(30, LIMIT + 1, 30): ### Kind of cheating, incrementing based on previous answers
# for n in range(100000, LIMIT + 1, 30):

    # print(f"\n==> (n = {n})")

    ### Get primes of >= n
    # primes_including_n = [i for i in yield_primes(n)]
    

    
    ####################################################################
    ### Find n/φ(n) 
    # print(f"==> totient({n})")

    # relative_primes = {1}
    totient = 1
    current_n_on_tn = 0
    factors_of_n = factors(n)
    DICT_OF_FACTORS.update({ n:factors_of_n })
    # print(f"Factors of {n} = {factors_of_n}")

    # for i in range(2, n): ### Naive, all numbers
    for i in range(3, n, 2): ### Odd numbers only (coprimes cannot be even)

        # if (is_coprime_old(i, n)):
        # if (
        #     (abs(i - n) == 1) ### Consecutive numbers are always coprime
        #     or (n % i == 0) ### Account for not including 'a' as a factor of itself below (NOTE: Swapped around?)
        #     or is_coprime(i, factors_of_n) ### Run slowest check to last
        # ):
        if is_coprime_old_v2(i, factors_of_n, n):
        # if is_coprime(i, n):
            # relative_primes.add(i)
            totient += 1

            current_n_on_tn = n / totient
            # print(f"==> totient({n}): n/φ(n) for current iteration = {current_n_on_tn}")

            if (current_n_on_tn < MAX_N_ON_TN):
                # print(f"==> totient({n}): n/φ(n) fell below MAX_N_ON_TN ({MAX_N_ON_TN})")
                break

    # print(f"==> totient({n}): Relative primes = {relative_primes}")
    ####################################################################

    # current_n_on_tn = n/totient(n)
    # print(f"(n = {n}) current_n_on_tn = {current_n_on_tn}")

    if (current_n_on_tn > MAX_N_ON_TN):
        RESULT = n
        MAX_N_ON_TN = current_n_on_tn

        print(f"==> (n = {n}) New highest n/φ(n) found: {MAX_N_ON_TN}")


### END MAIN LOOP (n)
####################################################################

print(f"\n==> n = {RESULT} produces a maximum n/φ(n) ({MAX_N_ON_TN}) for n ≤ {LIMIT}.")

