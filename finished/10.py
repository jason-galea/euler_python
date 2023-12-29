#!/usr/bin/env python3

def primes(i):		# Accepts int, yields all primes below and including 'i'
	arr = [True] * (i + 1)
	for x in range(2,i + 1):
		if arr[x]:
			yield x

			for y in range(x,i + 1,x):
				arr[y] = False

result = 0

for x in primes(2000000):
	result += x

print(result)
