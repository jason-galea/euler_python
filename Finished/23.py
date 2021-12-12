
def sumOfDivisors(n):
    sumOfDivisors = 1
    for i in range(2, int(n/2) + 1): # Find divisors
        if (n % i == 0):
            sumOfDivisors += i
    return sumOfDivisors

abundants = []
abundantSums = set()

for i in range(12, 28124):
    if not ((i % 2 == 0) or (i % 5 == 0)): continue # Free performance
    if not (i < sumOfDivisors(i)): continue # If not abundant

    print(f"Found adundant number {i}, checking sums...")
    abundants.append(i)
    for a in abundants:
        abundantSums.add(i + a)

resultSet = set(range(1, 28124)).difference(abundantSums)
print(f"Result = {sum(resultSet)}") # 4179871
