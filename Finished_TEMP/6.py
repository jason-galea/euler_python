#!/usr/bin/env python3

sum = 0
sum_of_squares = 0

for x in range(1,101):
	sum += x
	sum_of_squares += x**2

print(sum**2 - sum_of_squares)
