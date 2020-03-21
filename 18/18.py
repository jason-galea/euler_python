#!/usr/bin/env python3
# from functions import *

tri = [
                             [75],
                           [95, 64],
                         [17, 47, 82],
                       [18, 35, 87, 10],
                      [20, 4, 82, 47, 65],
                     [19, 1, 23, 75, 3, 34],
                   [88, 2, 77, 73, 7, 63, 67],
                 [99, 65, 4, 28, 6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
          [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
      [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

largest_path = 0
largest_path_chain = []

# For each permutation (Eg, "0101"), interpret each character as a path.
for i in range(2**(len(tri) - 1)) :
    permutation = str(bin(i))[2:]

    # Adding leading zero characters. Eg, "1" --> "001"
    while len(permutation) < (len(tri) - 1):
        permutation = "0" + permutation
    
    current_row = 0
    current_pos = 0
    current_chain = []
    current_chain_total = tri[current_row][current_pos]

    print(current_chain_total, end =" ")
    current_chain.append(current_chain_total)

    for choice in permutation:
        current_row += 1
        if choice == "0":
            current_chain_total += tri[current_row][current_pos]
        else:   # choice == "1"
            current_pos += 1
            current_chain_total += tri[current_row][current_pos]

        print("+", tri[current_row][current_pos], end =" ")
        current_chain.append(tri[current_row][current_pos])
    
    # If value is greater than 'result', result = value
    print("=", current_chain_total)
    if current_chain_total > largest_path:
        largest_path = current_chain_total
        largest_path_chain = current_chain


# Print result
print("\nThe largest chain was:\n\t", largest_path_chain)
print("It gave a total value of:", largest_path)