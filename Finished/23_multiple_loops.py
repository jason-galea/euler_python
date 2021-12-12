
def sumOfDivisors(n):
    sumOfDivisors = 1
    for i in range(2, int(n/2) + 1): # Find divisors
        if (n % i == 0):
            sumOfDivisors += i
    return sumOfDivisors

def main():
    ### Get all abundant numbers
    abundants = []
    for i in range(12, 28124):
        if (i % 2 == 0) or (i % 5 == 0): # All abundants are multiples of 2 or 5
            if (i < sumOfDivisors(i)):
                abundants.append(i)
                # print(f"Found adundant number {i}")
    print(f"Found {len(abundants)} abundant numbers")

    ### Find every sum of two abundants
    abundantSums = set()
    lenAbundants = len(abundants)
    for i, aa in enumerate(abundants):
        # print(f"Generating sums including abundant number {i}/{lenAbundants}: {aa}")
        for j in range(i, lenAbundants):
            abundantSums.add(aa + abundants[j])

    ### Find all positives ints not in abundant sums
    result = set(range(1, 28124)).difference(abundantSums)
    # print(result)
    print(f"Sum of positive ints not expressible as two abundant numbers = {sum(result)}") # 4179871

if __name__ == "__main__":
    main()
