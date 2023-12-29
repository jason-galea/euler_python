#!/usr/bin/env python3

def main(n):
    nFactorial = 1
    sumOfDigits = 0

    for x in range(2, n): # Factorial
        nFactorial *= x
    for x in str(nFactorial):# Sum of digits
        sumOfDigits += int(x)

    print(f"Sum of digits in {nFactorial} is: {sumOfDigits}")

if __name__ == "__main__":
    # main(10)
    main(100)
