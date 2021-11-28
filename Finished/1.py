#!/usr/bin/env python3

y = 0
for x in range(1, 1000):
	if ((x % 3 == 0) or (x % 5 == 0)):
		y += x

print("\nResult is: ", y, "\n")
