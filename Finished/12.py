#!/usr/bin/env python3

def triangles(i):	# Accepts int, yields all triangle numbers below and including 'i'
	result = 0
	for x in range(0, i):
		result += x
		if result <= i:
			yield result

def factors(i):		# Accepts int, yields all factors of 'i', including 1 and 'i'
	result = []
	for x in range(1, int(i**(1/2) + 1)):
		if i % x == 0:
			if x != i**(1/2):
				result.append(x)
			result.append(int(i / x))
	result.sort()

	for x in result:
		yield x

threshold = 500

for t in triangles(10**9):
	if t >= 10**6:
		divs = 0
		for i in factors(t):
			divs += 1
#			print("Found %i to be a factor of %i" %(i, t))

		if divs >= threshold:
			print(">>> %i has %i or more divisors" %(t, threshold))
