#!/usr/bin/env python3

def collatz(i):		# Accepts int, yields collatz sequence starting from 'i'
	yield i
	while True:
		if i % 2 == 0:
			i /= 2
		else:
			i = (i * 3) + 1
		yield int(i)

		if i == 1:
			break
		
result = 0

for x in range(1, 1000000):
	length = 0
	for y in collatz(x):
		length += 1
	if length >= result:
		result = length
		print("%i produced the new longest Collatz chain of: %i" %(x, length))
