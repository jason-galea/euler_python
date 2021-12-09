# https://projecteuler.net/problem=762
# https://www.mail-archive.com/chat@forums.jsoftware.com/msg03978.html

class Grid:
    def __init__(self) -> None:
        self.grid = [ #TODO: Compress
            [],
            [],
            [],
            [True]
        ]
        self.possibleGrids = [] # Including duplicates
        self.uniqueGrids = 0

    def getIterations(self, n): # Generate all possible iterations for C(n)
        pass
        # Generate

    def saveIterations(self):
        pass

    def areMatchingGrids(self, g1, g2):
        pass

        



def main():
    myGrid = Grid()
    myGrid.getIterations

if __name__ == "__main__":
    main()