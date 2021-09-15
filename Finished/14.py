#!/usr/bin/env python3
from functions import *

result = 0

for x in range(1, 1000000):
	length = 0
	for y in collatz(x):
		length += 1
	if length >= result:
		result = length
		print("%i produced the new longest Collatz chain of: %i" %(x, length))
