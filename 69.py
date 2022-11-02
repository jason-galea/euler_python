def is_coprime(a, b): ### Assumes a < b

    ### NOTE: Should be iterating through primes here
    ### NOTE: We're trying

    ### If ANY common factors, return False
    for i in range(2, a + 1): ### Naive
        if (a % i == 0) and (b % i == 0):
            print(f"is_coprime({a}, {b}) == False")
            return False

    print(f"is_coprime({a}, {b}) == True")
    return True

def totient(n, debug=False):

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
    for n in range(2, limit + 1, 2):
    # for n in range(0, limit + 1, 10): ### Breaks "limit" < 30
        
        # if (is_prime(n)): continue ### TODO
        if (n % 3 != 0): continue ### All current answers are divisible by three

        current_t = totient(n)
        current_n_on_tn = n/current_t

        # print(f"(n = {n}): φ(n) = {current_t}")
        # print(f"(n = {n}): n/φ(n) = {current_n_on_tn}")

        if (current_n_on_tn > max_n_on_tn):
            result = n
            max_n_on_tn = current_n_on_tn

            # print(f"(n = {n}): max_n_on_tn = {max_n_on_tn}")
            # totient(n, debug=True)

    print(f"\nFor n ≤ {limit}, n/φ(n) produces a maximum at n = {result}")
    print(f"For n = {result}, n/φ(n) = {max_n_on_tn}")

if __name__ == "__main__":

    ### Best times!!!
    main(10)        ### 0m00.013s
    # main(100)       ### 0m00.013s
    # main(500)       ### 0m00.018s
    # main(1000)      ### 0m00.053s
    # main(5000)      ### 0m4.871s
    # main(10000)     ### 0m39.498s
    # main(50000)     ### 
    # main(100000)    ### 
    # main(500000)    ### 

    ### GOAL
    # main(1000000)   ### 
