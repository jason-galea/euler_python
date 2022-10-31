def n_over_totient_n(n):
    return n/totient(n)

def totient(n):

    # relative_primes = set()
    relative_primes = {1}
    
    # iterate over 1 --> n - 1
    for i in range(2, n + 1):
        if (n % i == 0):
            relative_primes.add(i)

    print(f"relative_primes of {n}: {relative_primes}")

    return len(relative_primes)


def find_maximum(max_n):
    current_maximum = 0

    for i in range(2, max_n + 1):

if __name__ == "__main__":
    find_maximum(10)
