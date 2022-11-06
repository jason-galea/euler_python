def factors(i): ### Accepts int, returns set of factors (excluding 1 and i)

    # print(f"Finding factors of {i}")
    # set_of_factors = []
    set_of_factors = set()
    sqrt_i = int(i**0.5) ### Ignore floating point

    for j in range(2, sqrt_i + 1): ### Ignore 1
        if (i % j == 0):

            # print(f"Found factor of {i}: {j}")
            # set_of_factors.append(j)
            set_of_factors.add(j)

            if (j != sqrt_i): ### Only add matching factor if not square root
                # print(f"Found factor of {i}: {j}")
                # set_of_factors.append(int(i / j))
                set_of_factors.add(int(i / j))

    # print(f"Factors of {i} = {set_of_factors}")
    return set_of_factors

def is_coprime_find_factors_first(i, n):
    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    factors_of_i = factors(i)
    # print(f"Factors of {i} = {factors_of_i}")

    for factor in factors_of_i:
        if (n % factor == 0):
            return False

    return True

def is_coprime_find_and_check_factors(a, b): ### If ANY common factors, return False (Assumes a < b)
    # print(f"==> \tis_coprime({a}, {b})")

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

def is_coprime_precompute_factors_of_n(i, factors_of_n, n): ### Returns True if 'i' is cleanly divisible by any factor in given set
    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    for factor in factors_of_n:
        if (i % factor == 0):
            return False

    return True

def is_coprime_precompute_all_factors(i, n): ### Returns True if 'i' is cleanly divisible by any factor in given set
    if (abs(i - n) == 1): return True ### Consecutive numbers are always coprime
    if (n % i == 0): return False ### Account for not including 'a' as a factor of itself below

    for factor_of_i in DICT_OF_FACTORS[i]:
        if (factor_of_i in DICT_OF_FACTORS[n]):
            return False

    return True

###################################################################
### "MAIN"
### Best times!!!
LIMIT = 10         ### 0m00.013s           ### Answer = 6
# LIMIT = 50         ### 0m00.013s           ### Answer = 30
# LIMIT = 100        ### 0m00.013s           ### Answer = 30
# LIMIT = 500        ### 0m00.018s           ### Answer = 210
# LIMIT = 1000      ### 0m00.028s           ### Answer = 210
# LIMIT = 5000       ### 0m00.152            ### Answer = 2310
# LIMIT = 10000      ### 0m00.661s           ### Answer = 2310
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
for n in range(2, LIMIT + 1): ### "Naive", every number. Required for DICT_OF_FACTORS to be effective

    # print(f"\n==> (n = {n})")
    
    ####################################################################
    ### BEGIN "Find n/φ(n)" LOOP (i) 
    totient = 1
    current_n_on_tn = 0
    # factors_of_n = factors(n)
    # DICT_OF_FACTORS.update({ n:factors_of_n })
    # print(f"Factors of {n} = {factors_of_n}")

    for i in range(2, n): ### Naive, all numbers
    # for i in range(3, n, 2): ### Odd numbers only (coprimes cannot be even)

        if is_coprime_find_factors_first(i, n):
        # if is_coprime_find_and_check_factors(i, n):
        # if is_coprime_precompute_factors_of_n(i, factors_of_n, n):
        # if is_coprime_precompute_all_factors(i, n):
            totient += 1
            current_n_on_tn = n / totient
            # print(f"==> totient({n}): n/φ(n) for current iteration = {current_n_on_tn}")

            # if (current_n_on_tn == MAX_N_ON_TN): print(f"\n==> (n = {n}) matches current best n/φ(n) {MAX_N_ON_TN}")
            if (current_n_on_tn < MAX_N_ON_TN):
                # print(f"==> totient({n}): n/φ(n) fell below MAX_N_ON_TN ({MAX_N_ON_TN})")
                break

    ### END "Find n/φ(n)" LOOP (i) 
    ####################################################################

    # current_n_on_tn = n/totient(n)
    print(f"\n==> (n = {n}) φ({n}) = {totient}")

    if (current_n_on_tn > MAX_N_ON_TN):
        RESULT = n
        MAX_N_ON_TN = current_n_on_tn

        print(f"==> (n = {n}) New highest n/φ(n) found: {MAX_N_ON_TN}")

### END MAIN LOOP (n)
####################################################################

print(f"\n==> n = {RESULT} produces a maximum n/φ(n) ({MAX_N_ON_TN}) for n ≤ {LIMIT}.")

