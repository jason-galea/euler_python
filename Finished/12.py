#!/usr/bin/env python3
from functions import *

threshold = 500

for t in triangles(10**9):
	if t >= 10**6:
		divs = 0
		for i in factors(t):
			divs += 1
#			print("Found %i to be a factor of %i" %(i, t))

		if divs >= threshold:
			print(">>> %i has %i or more divisors" %(t, threshold))
