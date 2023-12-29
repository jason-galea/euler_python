#!/usr/bin/python3

size = int(input("\nEnter the size of the square array: ")) + 1
arr = [[0] * size] * size
arr[size - 1] = [1] * size

for x in arr:
    x[size - 1] = 1

for row in range(size - 2, -1, -1):
    for col in range(size - 2, -1, -1):
        arr[row][col] = (arr[row + 1][col]) + (arr[row][col + 1])

print("There are %s possible paths in this grid.\n" %(arr[0][0]))
