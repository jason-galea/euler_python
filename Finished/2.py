#!/usr/bin/env python3

fib = sum = a = 0
b = 1

while (a + b < 4000000):
	fib = a + b
	if (fib % 2 == 0):
		sum += fib

	a = b
	b = fib

print("\nThe result is ", sum, "\n")

