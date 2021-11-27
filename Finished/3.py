#!/usr/bin/env python3

def sqrt(i):
	return i**(1/2)

def primes(i):		# Accepts int, yields all primes below and including 'i'
	arr = [True] * (i + 1)
	for x in range(2,i + 1):
		if arr[x]:
			yield x

			for y in range(x,i + 1,x):
				arr[y] = False

n = 600851475143
max = 0

for p in primes(int(n**(1/2))):
	if n % p == 0:
		max = p


print(max)
