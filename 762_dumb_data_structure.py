# https://projecteuler.net/problem=762
# https://www.mail-archive.com/chat@forums.jsoftware.com/msg03978.html

def C(divisions): # C(n)
    possibleGrids = [[]] * divisions
    possibleGrids[0] = [ # All NEWLY possible grids for C(0)
            [ # One possible grid for C(0)
                "1000"
                # ,"1100"
            ]
        ]
    
    uniqueGrids = 0

    ### Find all possible grids for current division limit 'n'
    for n in range(divisions):

        # For each grid in C(n), find NEWLY possible divisions
        for gi, grid in enumerate(possibleGrids[n]): # Eg ["1000"] for C(0)
            # tempGrid = grid.copy()
            # tempGrid.append("0000")
            grid.append("0000") # Eg ["1000", "0000"]

            # For each row in grid
            for ri, row in enumerate(grid): # Eg "1000"

                # For each amoeba in row, test subsequent amoeba positions
                for ci, char in enumerate(row): # Eg "1"

                    # TODO: If char part of 2nd last row, final row is empty and will always succeed
                    # if (ri == len(grid) - 2):
                    #     pass

                    # If both subsequent amoebas are valid, save grid
                    if (
                        (char == "1") # Char is amoeba
                        and ((grid[ri + 1][ci]) != "1")
                        and ((grid[ri + 1][(ci + 1) % 4]) != "1")
                    ):
                        # "1000" # row[ci] = row[0..3]
                        # "?000" # grid[ri + 1][ci]

                        # "1000" # row[ci] = row[0..3]
                        # "0?00" # grid[ri + 1][(ci + 1) % 4]

                        tempGrid = grid.copy()
                        tempList = list(tempGrid[ri + 1]) # "0000" --> ["0", "0", "0", "0"]

                        tempList[ci] = "1"
                        tempList[ci + 1] = "1"

                        tempGrid[ri + 1] = "".join(tempList)
                        possibleGrids[n+1].append(tempGrid)
                        # FIXME: Use tempGrid for the entire grid loop
                        # grid.append("0000") fucks it all up



    ### De-duplicate possible grids
    pass

    print(possibleGrids)
    # print(uniqueGrids)


if __name__ == "__main__":
    C(2)
    # C(10)
    # C(20)
    # C(100)
    # C(100000)