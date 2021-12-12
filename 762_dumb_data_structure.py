# https://projecteuler.net/problem=762
# https://www.mail-archive.com/chat@forums.jsoftware.com/msg03978.html

def C_bloated(divisions):
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

def createPossibleGrid(baseGrid, ri, ci):
    # Accepts grid + coordinates for amoeba with known possible division positions
    newPossibleGrid = baseGrid.copy()

    # TODO: If final row, add new final row
    if ():
        pass
    
    # TODO: Modify existing row
    pass

    return newPossibleGrid

def C(n):
    possibleGridsPerDivision = [[]] * (n + 1) # Container for all possibilities per division
    possibleGridsPerDivision[0] = [ # All NEWLY possible grids for C(n)
            [ # Pre-populate C(0)
                "1000"
            ]
        ]
    
    uniqueGrids = 0

    for i in range(1, n + 1):
        # Copy all possible grids from C(n - 1)
        possibleGridsPerDivision[i] = possibleGridsPerDivision[i - 1].copy()

        for grid in possibleGridsPerDivision[i]: # ["1000", ""]

            # For each grid, find all new possible grids 
            for ri, row in enumerate(grid): # "1000"
                for ci, char in enumerate(row): # "1"
                    if (char != "1"): continue # If not amoeba break condition

                    # If amoeba in final row, new grid found
                    if (ri == len(grid) - 1):
                        # possibleGridsPerDivision[i].append(createPossibleGrid(grid, ri, ci))
                        newRow = "0000"
                        newRow[ci] = "1"
                        newRow[ci + 1] = "1"
                        possibleGridsPerDivision.append(grid.copy().append(newRow))

                    # If subsequent amoeba positions are possible, new grid found
                    if (grid[ri + 1][ci] == "0") and (grid[ri + 1][ci + 1] == "0"):
                        # possibleGridsPerDivision[i].append(createPossibleGrid(grid, ri, ci))
                        newGrid = grid.copy()
                        newGrid[ri + 1][ci] = "1"
                        newGrid[ri + 1][ci + 1] = "1"
                        possibleGridsPerDivision.append(newGrid)

        pass

if __name__ == "__main__":
    C(2)
    # C(10)
    # C(20)
    # C(100)
    # C(100000)