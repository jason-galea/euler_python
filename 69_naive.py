def is_coprime(a, b):
    for i in range(2, a + 1): # Assume a < b
        if (a % i == 0) and (b % i == 0):
            return False

    return True

def totient(n):
    relative_primes = { i for i in range(2, n) if is_coprime(i, n) }
    #print(f"Relative primes of {n} = {relative_primes}")

    return len(relative_primes) + 1 ### +1 for assuming

def find_max_n_over_t(max_n):
    max_n_over_t = 0
    n_that_produces_max_n_over_t = 0

    for n in range(2, max_n + 1):
        current_t = totient(n)
        current_n_over_t = round(n/current_t, 4)

        #print(f"φ{n} = {current_t}")
        #print(f"{n}/φ({n}) = {current_n_over_t}")

        if (current_n_over_t > max_n_over_t):
            max_n_over_t = current_n_over_t
            n_that_produces_max_n_over_t = n
            print(f"New maximum n/φ(n) found! {n}/φ({n}) = {current_n_over_t}")

    print(f"\nmax_n_over_t = {max_n_over_t}")
    print(f"n_that_produces_max_n_over_t = {n_that_produces_max_n_over_t}")

if __name__ == "__main__":
    find_max_n_over_t(500)
    #find_max_n_over_t(1000)
    #find_max_n_over_t(1000000)
