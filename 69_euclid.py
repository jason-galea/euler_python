def factors(i): ### Returns factors (excluding i)
    #set_of_factors = set()
    set_of_factors = {1}
    sqrt_i = int(i**0.5) ### Ignore floating point

    for j in range(2, sqrt_i + 1): ### Ignore 1
        if (i % j == 0):

            set_of_factors.add(j)

            if (j != sqrt_i):
                set_of_factors.add(int(i / j))

    # print(f"Factors of {i} = {set_of_factors}")
    return set_of_factors

def gcd(x, y): ### AKA. highest common factor
    if (x == y): return x

    # factors_of_x = factors(x)
    # factors_of_y = factors(y)
    hcf = 0

    ### TODO: Implement DICT_OF_FACTORS
    for i in factors(x):
        if (i in factors(y)) and (i > hcf):
            hcf = i

    return hcf

def is_coprime_euclid_subtract(high, low):

    ### Easy exits
    if (n - i == 1): return True ### Consecutive numbers == coprime
    if (n % i == 0): return False

    # print(f"START: gcd({high}, {low})")

    while True:
        if (low == high): break
        if (low == 1): ### Shortcut, gcd(x, 1) = 1
            return True

        diff = high - low
        #print(f"{high} - {low} = {diff}")
        #print(f"gcd({high}, {low})")

        ### Prepare vars for next iteration
        ### NOTE: Equal values will be caught immediately
        high = max(diff, low)
        low = min(diff, low)

    ### no return logic yet
    print(f"END: gcd({high}, {low})")

    # print(f"Highest common factor = {gcd(high, low)}")
    return ( gcd(high, low) == 1 )



### MAIN
# LIMIT = 10
# LIMIT = 50
# LIMIT = 100
# LIMIT = 500
LIMIT = 1000
# LIMIT = 5000
# LIMIT = 10000
# LIMIT = 50000
# LIMIT = 100000

RESULT = 0
MAX_N_ON_TN = 0
DICT_OF_FACTORS = {}

for n in range(2, LIMIT + 1):
    
    totient = 1
    current_n_on_tn = 0

    for i in range(2, n):
        print(f"\nAre {n} & {i} coprime?")
        if is_coprime_euclid_subtract(n, i):

            totient += 1
            current_n_on_tn = n / totient
            # print(f"==> (n = {n})\tn/φ(n) for current iteration = {current_n_on_tn}")

            if (current_n_on_tn < MAX_N_ON_TN):
                # print(f"==> (n = {n})\tn/φ(n) fell below MAX_N_ON_TN ({MAX_N_ON_TN})")
                break

    if (current_n_on_tn > MAX_N_ON_TN):
        RESULT = n
        MAX_N_ON_TN = current_n_on_tn

        print(f"==> (n = {n})\t New highest n/φ(n) found: {MAX_N_ON_TN}")

print(f"\n==> n = {RESULT} produces a maximum n/φ(n) ({MAX_N_ON_TN}) for n ≤ {LIMIT}.")
### END MAIN
