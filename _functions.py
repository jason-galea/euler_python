...

def sqrt(i):
	return i**(1/2)

def rev_str(s):
	return ''.join(reversed(s))

def is_prime(i):
	for x in range(2, int(sqrt(i)) + 1):
		if i % x == 0:
			return False
	return True

def primes(i):		# Accepts int, yields all primes below and including 'i'
	arr = [True] * (i + 1)
	for x in range(2,i + 1):
		if arr[x]:
			yield x

			for y in range(x,i + 1,x):
				arr[y] = False

def triangles(i):	# Accepts int, yields all triangle numbers below and including 'i'
	result = 0
	for x in range(0, i):
		result += x
		if result <= i:
			yield result

def factors(i):		# Accepts int, yields all factors of 'i', including 1 and 'i'
	result = []
	for x in range(1, int(sqrt(i) + 1)):
		if i % x == 0:
			if x != sqrt(i):
				result.append(x)
			result.append(int(i / x))
	result.sort()

	for x in result:
		yield x

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

def factorial(i):	# Accepts int, returns int!
	if i == 0:
		return 1

	for x in range(i - 1, 1, -1):
		i *= x

	return i
