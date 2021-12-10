
def sumOfDivisors(n):
    sumOfDivisors = 1
    for i in range(2, int(n/2) + 1): # Find divisors
        if (n % i == 0):
            sumOfDivisors += i
    return sumOfDivisors

def main():
    ### Get all abundant numbers
    abundants = []
    for i in range(12, 28124, 2):
        if (i < sumOfDivisors(i)):
            abundants.append(i)
            print(f"Found adundant number {i}")
    for i in range(15, 28124, 10):
        if (i < sumOfDivisors(i)):
            abundants.append(i)
            print(f"Found adundant number {i}")
    print(f"Found {len(abundants)} abundant numbers")

    ### For every sum of abundants, remove sum from set of all posInts
    posInts = list(range(1, 28124))
    lenAbundants = len(abundants)
    for i, aa in enumerate(abundants):
        
        for j in range(i, lenAbundants):
            ab = abundants[j]
            sum = aa + ab
            # if (sum in posInts):
            try:
                posInts.remove(sum)
                # print(f"Removed {aa} + {ab} = {sum} from posInts[]")
            except:
                pass
    
    print(posInts)
    print(sum(posInts)) # 4179871

if __name__ == "__main__":
    main()
