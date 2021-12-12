# https://projecteuler.net/problem=762
# https://www.mail-archive.com/chat@forums.jsoftware.com/msg03978.html

def printGrid(grid): # ["1000", "1100"]
    out = [""] * 4
    
    # Unwrap
    for row in grid:
        for i in range(4):
            out[i] += row[i] 

    # Print horizontally, as shown on https://projecteuler.net/problem=762
    # print(f"Printing grid...")
    print()
    for i in range(3, -1, -1):
        print(out[i])

def createPossibleGrid(baseGrid, ri, ci):
    # Accepts grid + coordinates for amoeba with known possible division positions
    newGrid = baseGrid.copy()
    finalRowIndex = len(newGrid) - 1

    if (ri == finalRowIndex):
        newGrid.append("0000")
    
    # Modify existing row ri + 1
    newRow = [char for char in newGrid[ri + 1]] # Eg ["0", "0", "0", "0"]
    newRow[ci] = "1"
    newRow[(ci + 1) % 4] = "1"
    newGrid[ri + 1] = "".join(newRow)

    return newGrid

def C(n):
    # n -= 1
    possibleGridsPerN = [[ # All NEWLY possible grids for C(n)
        [ # Pre-populate C(0)
            "1000"
        ]
    ]]
    uniqueGrids = set()
    # uniqueGrids.add("".join(possibleGridsPerN[0][0]))
    # This ^^^ string conversion is a horrific workaround
    # until I store the grids as immutable objects


    ### Find all possible grids for C(n)
    for i in range(1, n + 1): # n == i, effectively

        # Prepare container for possible grids of C(n)
        possibleGridsPerN.append([])

        # For each grid in C(n - 1), find all new possible grids 
        for grid in possibleGridsPerN[i - 1]: # ["1000", ""]
            for ri, row in enumerate(grid): # "1000"
                for ci, char in enumerate(row): # "1"
                    if (char != "1"): continue # If not amoeba break condition

                    # If amoeba in final row, new grid found
                    if (ri == len(grid) - 1):
                        newGrid = createPossibleGrid(grid, ri, ci)

                        possibleGridsPerN[i].append(newGrid)
                        # uniqueGrids.add("".join(newGrid))

                        continue

                    # If subsequent amoeba positions are possible, new grid found
                    if (grid[ri + 1][ci] == "0") and (grid[ri + 1][(ci + 1) % 4] == "0"):
                        newGrid = createPossibleGrid(grid, ri, ci)

                        possibleGridsPerN[i].append(newGrid)
                        # uniqueGrids.add("".join(newGrid))

                        continue

    ### Find all unique grids for C(n)
    for grid in possibleGridsPerN[n]:
        uniqueGrids.add("".join(grid))
        printGrid(grid)

    print(f"\nC({n}) = {len(uniqueGrids)}\n")

if __name__ == "__main__":
    # C(1)
    # C(2)
    # C(5)
    C(10)
    # C(11)
    # C(20)
    # C(100)
    # C(100000)