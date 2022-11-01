def is_a_factor(a, b):
    return (a % b == 0)

def is_relatively_prime(a, b):
    """
    Returns True if a & b are relatively prime, else returns False.
    (It is assumed that b == n from totient(), therefore a < b.)
    """
    for i in range(2, a + 1):
        if ( is_a_factor(i, a) and is_a_factor(i, b) ):
            return False

    return True

def totient(n):

    relative_primes = {1}

    for i in range(2, n):
        # if (n % i == 0):
        if (n % i != 0):
            relative_primes.add(i)

    print(f"relative_primes of {n}: {relative_primes}")

    return len(relative_primes)

def find_maximum_totient_over_n(max_n):
    maximum_n_over_totient = 0
    n_that_produces_maximum_n_over_totient = 0

    for n in range(2, max_n + 1):
        current_totient = totient(n)
        current_n_over_totient = round(n/current_totient, 4)

        # print(f"φ{n} = {totient(n)}")
        # print(f"{n}/φ({n}) = {n_over_totient_n(n)}")
        print(f"{n}/φ({n}) = {current_n_over_totient}")

        if (current_n_over_totient > maximum_n_over_totient):
            maximum_n_over_totient = current_n_over_totient
            n_that_produces_maximum_n_over_totient = n
            # print(f"New maximum n/φ(n) found! {n}/φ({n}) = {current_n_over_totient}")

    print(f"\nmaximum_n_over_totient = {maximum_n_over_totient}")
    print(f"n_that_produces_maximum_n_over_totient = {n_that_produces_maximum_n_over_totient}")

if __name__ == "__main__":
    find_maximum_totient_over_n(10)
    # find_maximum_totient_over_n(1000)
    # find_maximum_totient_over_n(1000000)
