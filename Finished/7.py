#!/usr/bin/env python3

def primes(i):		# Accepts int, yields all primes below and including 'i'
	arr = [True] * (i + 1)
	for x in range(2,i + 1):
		if arr[x]:
			yield x

			for y in range(x,i + 1,x):
				arr[y] = False

end_count = 10001
prime_count = 0

for x in primes(10**6):
	prime_count += 1
	if prime_count == end_count:
		print("Prime number", end_count, "is:", x)
		exit()
