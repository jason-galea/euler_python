#!/usr/bin/env python3

# def sum_of_divisors(n): # Add divisors together when found
#     result = 0
#     for i in range(2, int(n/2) + 1): # Find divisors
#         if (n % i == 0):
#             result += i
#     return result

def sum_of_divisors(n): # Find all divisors THEN sum
    divisors = [1]
    for i in range(2, int(n/2) + 1): # Find divisors
        if (n % i == 0):
            divisors.append(i)
    return sum(divisors)

# def main(n): # Add amicables together when found
#     result = 0
#     for i in range(2, n): # Skip 0 and 1
#         sumDiv = sum_of_divisors(i)
#         if (i == sum_of_divisors(sumDiv)) and (i != sumDiv):
#             print(f"Found new amicable number {i} ({sumDiv})")
#             result += sumDiv
#     print(f"Sum of all amicable numbers <{n} is: {result}")

def main(n): # Find all amicables THEN sum
    amicables = []
    for i in range(2, n, 2): # Skip 0 and 1
        if i not in amicables:
            sumDiv = sum_of_divisors(i)
        if (i == sum_of_divisors(sumDiv)) and (i != sumDiv):
            print(f"Found new amicable numbers {i} amd {sumDiv}")
            amicables.append(i)
            amicables.append(sumDiv)
    print(f"Sum of all amicable numbers <{n} is: {sum(amicables)}")

if __name__ == "__main__":
    main(10000)
