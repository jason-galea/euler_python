#!/usr/bin/env python3
from functions import *

n = 600851475143
max = 0

for p in primes(int(sqrt(n))):
	if n % p == 0:
		max = p


print(max)
