#!/usr/bin/env python3
from functions import *

result = 0

for x in primes(2000000):
	result += x

print(result)
