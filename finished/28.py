def find_sum_of_diagonals(max_grid_size):
    """
    Expects an odd number
    """

    DEBUG = True
    # DEBUG = False
    
    sum = 1
    current_grid_size = 1
    previous_number = 1
    if DEBUG: print(f"previous_number = {previous_number}")

    while True:
        current_grid_size += 2
        if DEBUG:  print(f"current_grid_size = {current_grid_size}")

        ### Find & add diagonals from current iteration
        ### NOTE: Increment between diagonals to be added == current_grid_size -1
        ### NOTE: E.G: Corners of top row of grid size 5 are 21 & 25
        ### NOTE: Increment == 25 - 21 == 4 == current_grid_size - 1
        for _ in range(4):
            previous_number += current_grid_size - 1
            if DEBUG:  print(f"previous_number = {previous_number}")

            sum +=  previous_number


        if (current_grid_size >= max_grid_size):
            # return sum
            print(f"Sum of diagonal numbers in grid of size {max_grid_size} == {sum}")
            exit()

        

        

if __name__ == "__main__":
    # find_sum_of_diagonals(3)
    # find_sum_of_diagonals(5) ### Should return 101
    # find_sum_of_diagonals(101)
    find_sum_of_diagonals(1001)
