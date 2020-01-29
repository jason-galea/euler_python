#!/usr/bin/env python3
from functions import *

n = int(input("\nEnter n: "))
digits = 2**n
result = 0

for x in str(digits):
    result += int(x)

print("\nThe sum of the digits in 2^%s or %s, equals %s\n" %(n, digits, result))