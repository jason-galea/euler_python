#!/usr/bin/env python3

for x in range(10**8, 10**9, 20):
	result = 0
	for y in range(1, 21):
		if x % y == 0:
			result += 1
	if result >= 19:
		print(x, result)
	if result == 20:
		print("FOUND: ", x, result)
		exit()
