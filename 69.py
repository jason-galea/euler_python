def factors(i): ### Accepts int, returns set of factors (excluding 1 and i)

    set_of_factors = set()
    sqrt_i = int(i**0.5) ### Ignore floating point

    for j in range(2, sqrt_i + 1): ### Ignore 1
        if (i % j == 0):

            set_of_factors.add(j)

            if (j != sqrt_i): ### Only add matching factor if not square root
                set_of_factors.add(int(i / j))

    # print(f"Factors of {i} = {set_of_factors}")
    return set_of_factors

def is_coprime_find_factors_first(i, n):
    # print(f"==> (n = {n})\tThis function calculates the factors of 'i' ({i})")

    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    factors_of_i = factors(i)

    for factor in factors_of_i:
        if (n % factor == 0):
            return False

    return True

def is_coprime_find_and_check_factors(i, n): ### If ANY common factors, return False (Assumes a < b)
    # print(f"==> (n = {n})\tThis function calculates the factors of 'i' ({i})")

    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    sqrt_i = i**0.5 ### Could be a float

    ### Find & check factors of 'a'
    for j in range(2, int(sqrt_i + 1)):

        if (i % j == 0):

            if (n % j == 0):
                return False

            if (j != sqrt_i) and (n % (int(j/i)) == 0): ### Check matching factor if not square root
                return False

    return True

def is_coprime_precompute_factors_of_n(i, factors_of_n, n):
    # print(f"==> (n = {n})\tThis function expects the factors of 'n' ({n}) to be precalculated")

    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    for factor in factors_of_n:
        if (i % factor == 0):
            return False

    return True

def is_coprime_precompute_all_factors(i, n):
    # print(f"==> (n = {n})\tThis function expects the factors of 'n' ({n}) & 'i' ({i}) to be precalculated")

    if (n - i == 1): return True ### Consecutive numbers are always coprime
    # if (): return True
    if (n % i == 0):
        # print(f"==> (n = {n})\tn ({n}) is divisible by i ({i})")
        return False ### Account for not including 'a' as a factor of itself below

    for factor_of_i in DICT_OF_FACTORS[i]:
        if (factor_of_i in DICT_OF_FACTORS[n]):
            # print(f"==> (n = {n})\tFound common factor of {n} and {i} = {factor_of_i}")
            return False

    return True

###################################################################
### "MAIN"
### Find N that produces highest n/φ(n)
### φ(n) is the count of numbers <= n, that are coprime with n
### (AKA, N with most factors and lowest value)

### NOTE: The common factors that fail "is_coprime" are ALWAYS* prime (*Are you 100% certain?)
### IDEA:
### 1. Get list of all primes < n
### 2. Iterate over these primes find common factors for n
### 3. Populate DICT_OF_FACTORS with { n: these (prime) common factors }
### NOTE: The above assumption assumes the common factor that fails "is_coprime" is ALWAYS prime, 100% of the time.
### NOTE: One way to handle this assumption is to simply check the "prime common factors" first
### NOTE: After checking "prime common factors", continue to check ALL common factors

### Best times!!!
# LIMIT = 10          ### 0m00.013s, n = 6, n/φ(n) = 3.0
# LIMIT = 50          ### 0m00.013s, n = 30, n/φ(n) = 3.75  
# LIMIT = 100         ### 0m00.013s, n = 30, n/φ(n) = 3.75
# LIMIT = 500         ### 0m00.018s, n = ???, n/φ(n) = ???
# LIMIT = 1000        ### 0m00.028s, n = ???, n/φ(n) = ???
LIMIT = 5000        ### 0m00.152s, n = ???, n/φ(n) = ???
# LIMIT = 10000       ### 0m00.661s, n = ???, n/φ(n) = ???
# LIMIT = 50000       ### 0m27.154s, n = ???, n/φ(n) = ???
# LIMIT = 100000      ### 2m30.528s, n = ???, n/φ(n) = ???
# LIMIT = 500000      ### 0m00.013s, n = ???, n/φ(n) = ???

### GOAL
# LIMIT = 1000000     ### 0m00.013s, n = ???, n/φ(n) = ???

RESULT = 0
MAX_N_ON_TN = 0
DICT_OF_FACTORS = {}

####################################################################
### BEGIN MAIN LOOP (n)
for n in range(2, LIMIT + 1): ### "Naive", every number. Required for DICT_OF_FACTORS to be effective

    # print(f"\n==> (n = {n})")
    
    ####################################################################
    ### BEGIN "Find n/φ(n)" LOOP (i) 
    totient = 1
    current_n_on_tn = 0
    DICT_OF_FACTORS.update({ n:factors(n) }) ### Only required for "is_coprime_precompute_all_factors()"
    # print(f"Factors of {n} = {factors(n)}")

    ### Early exit for 

    for i in range(2, n): ### Naive, all numbers
    # for i in range(3, n, 2): ### Odd numbers only (coprimes cannot be even)

        # print(f"==> (n = {n})\tis_coprime({i}, {n})")
        # if is_coprime_find_factors_first(i, n):
        # if is_coprime_find_and_check_factors(i, n):
        # if is_coprime_precompute_factors_of_n(i, factors(n), n):
        if is_coprime_precompute_all_factors(i, n):
            # print(f"==> (n = {n})\tFound coprime of {n}, {i}")

            totient += 1
            current_n_on_tn = n / totient
            # print(f"==> (n = {n})\tn/φ(n) for current iteration = {current_n_on_tn}")

            if (current_n_on_tn < MAX_N_ON_TN):
                # print(f"==> (n = {n})\tn/φ(n) fell below MAX_N_ON_TN ({MAX_N_ON_TN})")
                break

    ### END "Find n/φ(n)" LOOP (i) 
    ####################################################################

    # current_n_on_tn = n/totient(n)
    # print(f"\n==> (n = {n}) φ({n}) = {totient}")

    if (current_n_on_tn > MAX_N_ON_TN):
        RESULT = n
        MAX_N_ON_TN = current_n_on_tn

        print(f"==> (n = {n})\t New highest n/φ(n) found: {MAX_N_ON_TN}")

### END MAIN LOOP (n)
####################################################################

print(f"\n==> n = {RESULT} produces a maximum n/φ(n) ({MAX_N_ON_TN}) for n ≤ {LIMIT}.")

