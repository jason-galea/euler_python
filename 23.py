#!/usr/bin/env python3

def sum_of_divisors(n): # Find all divisors THEN sum
    divisors = [1]
    for i in range(2, int(n/2) + 1): # Find divisors
        if (n % i == 0):
            divisors.append(i)
    return sum(divisors)

def main():
    # Get all abundant numbers
    abundants = []
    # abundantHashes = []
    for i in range(12, 28124):
        if (i < sum_of_divisors(i)):
            abundants.append(i)
            # abundantHashes.append(hash(i))
    print(f"Found {len(abundants)} abundant numbers")

    # For all positive integers, check if they can NOT be written as a sum of two abundants
    posIntsNotExpressibleAsTwoAbundants = []
    for i in range(1, 28124):
        iExpressibleAsTwoAbundants = False # Not yet known
        for abundant in abundants:
            if (i - abundant in abundants): # If it IS able to be written as two, break loop
                iExpressibleAsTwoAbundants = True
                break
            # if (hash(i - abundant) not in abundantHashes):
            #     break
        if (not iExpressibleAsTwoAbundants): # Then "i" made it through the loop without failure
            posIntsNotExpressibleAsTwoAbundants.append(i)

    
    print(f"Result: {sum(posIntsNotExpressibleAsTwoAbundants)}")

if __name__ == "__main__":
    main()
