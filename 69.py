def yield_primes(i):    ### Accepts int, yields all primes below and including 'i'
    arr = [True] * (i + 1)

    for x in range(2, i + 1):
        if arr[x]:
            yield x

            for y in range(x, i + 1, x):
                arr[y] = False

def is_coprime(a, b): ### If ANY common factors, return False (Assumes a < b)
    # print(f"==> \tis_coprime({a}, {b})")
    print(f"==> \t Are {a} & {b} coprime?")

    ### Early exits
    if (abs(a - b) == 1): return True ### Consecutive numbers are always coprime
    if (b % a == 0): return False ### Account for not including 'a' as a factor of itself below

    sqrt_a = a**0.5 ### Could be a float

    ### Find & check factors of 'a'
    for i in range(2, int(sqrt_a + 1)):
        print(f"==> \t\t Is {i} a factor?")

        if (a % i == 0):
            print(f"==> \t\t\t {i} is a factor of {a}")

            if (b % i == 0):
                print(f"==> \t\t\t {a} & {b} are not coprime (common factor {i})")
                return False

            if (i != sqrt_a) and (b % (int(a/i)) == 0): ### Check matching factor if not square root
                print(f"==> \t\t\t {a} & {b} are not coprime (common factor {i})")
                return False
                    
    print(f"==> \t\t\t {a} & {b} ARE coprime (No common factors found)")
    return True

def main(limit):
    """
    Find N that produces highest n/φ(n)
    φ(n) is the count of numbers <= n, that are coprime with n

    AKA, N with most factors and lowest value
    """

    RESULT = 0
    global MAX_N_ON_TN
    MAX_N_ON_TN = 0

    
    ####################################################################
    ### BEGIN MAIN LOOP (n)
    # for n in range(2, limit + 1): ### Naive, all numbers
    # for n in range(2, limit + 1, 2): ### Even numbers only (Target N will never be odd/prime)
    for n in range(10, limit + 1, 10): ### Kind of cheating, incrementing based on previous answers
    # for n in range(30, limit + 1, 30): ### Kind of cheating, incrementing based on previous answers
    # for n in range(100000, limit + 1, 30):

        print(f"\n==> (n = {n})")

        ### Get primes of >= n
        # primes_including_n = [i for i in yield_primes(n)]
        
        
        ####################################################################
        ### Find n/φ(n) 
        # print(f"==> totient({n})")

        # relative_primes = {1}
        totient = 1
        current_n_on_tn = 0

        # for i in range(2, n): ### Naive, all numbers
        for i in range(3, n, 2): ### Odd numbers only (coprimes cannot be even)

            if (is_coprime(i, n)):
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

    print(f"\n==> n = {RESULT} produces a maximum n/φ(n) ({MAX_N_ON_TN}) for n ≤ {limit}.")

if __name__ == "__main__":

    ### Best times!!!
    # main(10)        ### 0m00.013s           ### Answer = 6
    main(50)        ### 0m00.013s           ### Answer = 30
    # main(100)       ### 0m00.013s           ### Answer = 30
    # main(500)       ### 0m00.018s           ### Answer = 210
    # main(1000)      ### 0m00.028s           ### Answer = 210
    # main(5000)      ### 0m00.152            ### Answer = 2310
    # main(10000)     ### 0m00.661s           ### Answer = 2310
    # main(50000)     ### 0m27.154s           ### Answer = 30030 (5.2135)
    # main(100000)    ### 2m30.528s           ### Answer = 30030
    # main(500000)    ### 0m??.???s           ### Answer = ???

    ### GOAL
    # main(1000000)   ### 0m??.???s           ### Answer = ???
