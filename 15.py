#!/usr/bin/env python3
from functions import *

size = int(input("\nEnter a number for the size of the square array:\n")) + 1
arr = [[0] * size] * size



print("Printing nested array to show ")
for row in arr:
    print(row)
print()