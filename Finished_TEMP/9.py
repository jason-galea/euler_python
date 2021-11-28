#!/usr/bin/env python3

# loop 1000 -> 0 as b
	# loop b -> 0 as a
		# find c
		# if c is int, it is natural, so:
			# test if a + b + c = 1000

for b in range(1000, 0, -1):
	for a in range(b, 0, -1):
		c = a**2 + b**2
		if int(c**(1/2) + 0.5)**2 == c and a + b + c**(1/2) == 1000:
			c = int(c**(1/2))
			print("%i + %i + %i = 1000" %(a, b, c))
			print("Product ABC =", a*b*c)
