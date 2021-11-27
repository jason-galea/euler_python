#!/usr/bin/env python3

# Recieve size of array 
size = int(input("\nEnter the size of the square array: ")) + 1
    # +1 because this array represents vertices, not the literal square

# Create empty array
arr = [[0] * size] * size

# Set bottom and left edges all to "1", due to movement restrictions
arr[size - 1] = [1] * size
for x in arr:
    x[size - 1] = 1

# Main loop
for row in range(size - 2, -1, -1):
    for col in range(size - 2, -1, -1):
        # print("Cell [%s, %s] = %s" %(row, col, arr[row][col]))

        arr[row][col] = (arr[row + 1][col]) + (arr[row][col + 1])

        print("Cell [%s, %s] = %s" %(row, col, arr[row][col]))
    # break

print()


# Print completed grid, answer is at the top-left corner
for x in arr:
    print(x)

print("\nThere are %s possible paths in this grid.\n" %(arr[0][0]))
