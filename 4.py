#!/usr/bin/env python3
from functions import *

# Looping from 999 -> 100
	# Looping from x --> 100
		# If str(x * y) == rev_str(x * y)
		# Must be the largest palindrone of 2 3-digit numbers
			# Return str

result = 0

for x in range(999,99,-1):
	for y in range(x,99,-1):
		prod = x * y
		if str(prod) == rev_str(str(prod)) and prod >= result:
			result = prod

print(result)
