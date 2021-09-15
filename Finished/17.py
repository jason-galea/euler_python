#!/usr/bin/env python3
from functions import *

ones = ["", "one", "two", "three", "four"
    , "five", "six", "seven", "eight", "nine"
]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen"
    , "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
tens = ["", "", "twenty", "thirty", "forty"
    , "fifty", "sixty", "seventy", "eighty", "ninety"
]
output = [""]
result = 0

for x in range(1, 1001):
    if x < 10:
        output.append(ones[x])
    elif x >= 10 and x < 20:
        output.append(teens[(int(str(x)[1:]))])
    elif x >= 20 and x < 100:
        tens_digit = int(str(x)[:1])
        ones_digit = int(str(x)[1:])
        output.append(tens[tens_digit] + " " + ones[ones_digit])
    elif x >= 100 and x < 1000:
        if x % 100 == 0:
            output.append(ones[int(str(x)[:1])] + " hundred")
        else:
            hundreds_digit = int(str(x)[:1])
            while x > 100:
                x -= 100
            output.append(ones[hundreds_digit] + " hundred and " + output[x])  
    elif x == 1000:
        output.append("one thousand")

for x in output:
    print(x)
    result += len(str(x).replace(" ", ""))
    # print(x)

print("\nTotal characters printed = %s\n" %(result))