#!/usr/bin/env python3
from functions import *

# Recieve size of array 
size = int(input("\nEnter the size of the square array:\n")) + 1
    # +1 because this array represents vertices, not the literal square

# Create empty array
arr = [[0] * size] * size

# Set bottom and left edges all to "1", due to movement restrictions
arr[size - 1] = [1] * size
for x in arr:
    x[size - 1] = 1




# Print completed grid, answer is at the top-left corner
for x in arr:
    print(x)
