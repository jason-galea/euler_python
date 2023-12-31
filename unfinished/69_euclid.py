def is_coprime_euclid_divide(high, low): ### Does gcd(high, low) = 1?
    # print(f"START: gcd({high}, {low})")

    if (high - low == 1): return True ### Consecutive numbers are always coprime
    if (high % low == 0): return False ### gcd(high, low) == low != 1

    while True:
        remainder = high % low

        ### "low" from the PREVIOUS iteration is the final divisor
        ### Therefore: low == gcd(high, low)
        ### Therefore: if (low == 1) --> "high" & "low" are coprime
        if (remainder == 0): return (low == 1)

        high = max(remainder, low)
        low = min(remainder, low)


def main(LIMIT):
    RESULT = 0
    MAX_N_ON_TN = 0
    # DICT_OF_FACTORS = {}

    ### START MAIN LOOP
    # for n in range(2, LIMIT + 1): ### "Naive", all numbers
    # for n in range(2, LIMIT + 1, 2): ### Even numbers only (Target N will never be odd/prime)
    for n in range(10, LIMIT + 1, 10): ### Kind of cheating
    # for n in range(30, LIMIT + 1, 30): ### Kind of cheating
    # for n in range(100000, LIMIT + 1, 30):

        totient = 1
        current_n_on_tn = 0

        for i in range(2, n):
            # print(f"\nAre {n} & {i} coprime?")

            # if is_coprime_euclid_subtract(n, i):
            if is_coprime_euclid_divide(n, i):
                # print("TRUE")

                totient += 1

                ### Early exit from current iteration
                current_n_on_tn = n / totient
                # print(f"==> (n = {n})\tn/φ(n) for current iteration = {current_n_on_tn}")

                if (current_n_on_tn < MAX_N_ON_TN):
                    # print(f"==> (n = {n})\tn/φ(n) fell below MAX_N_ON_TN ({MAX_N_ON_TN})")
                    break
            
            # else:
            #     print("FALSE")

        if (current_n_on_tn > MAX_N_ON_TN):
            RESULT = n
            MAX_N_ON_TN = current_n_on_tn
            print(f"==> (n = {n})\t New highest n/φ(n) found: {MAX_N_ON_TN}")

    ### END MAIN LOOP

    print(f"\n==> n = {RESULT} produces a maximum n/φ(n) of {MAX_N_ON_TN} for n ≤ {LIMIT}.")



if __name__ == "__main__":
    # main(10)
    # main(50)
    # main(100)
    # main(500)
    # main(1000)
    main(5000)
    # main(10000)
    # main(50000)
    # main(100000)
