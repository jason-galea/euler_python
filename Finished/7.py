#!/usr/bin/env python3
from functions import *

end_count = 10001
prime_count = 0

for x in primes(10**6):
	prime_count += 1
	if prime_count == end_count:
		print("Prime number", end_count, "is:", x)
		exit()
