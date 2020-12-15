
# Return True if the cell at given position (row, colum) is infected
def isInfected(grid, r, c ) :
    return grid[r][c] == 1

# Return True if the cell at given position (row, colum) will be infected after contamination
def willBeInfected(grid, r, c) :

    # 1- Check if any VETICAL CONTAMINATION   (top cell and buttom cells are  infected)
    verticalCont = False
    # TODO  !!!!
    if isInfected(grid, r, c ) :
        verticalCont = True
    # 2- Check if any HORIZONTA CONTAMINATION  (left cell and right cells are  infected)
    horizontalCont = False
     # TODO  !!!!
    if grid[r][c-1] == 1 and 1 == grid[r][c+1]:
        horizontalCont = True
    
    # 3- cell infected if vertical or horizontal contamination
    return verticalCont or horizontalCont

# Return the list of cell that  WILL BE  infected after contamination
# Return is an array of cell positions, each position is an array  [row, column]
def getNextInfectedCells(grid) :
    grid.append(grid[0])
    rowNb = len(grid)
    columnNb = len(grid[0])
    result = []
   
     # TODO  !!!!
    
    for r in range(rowNb-1):
        leter = []
        for c in range(columnNb-1):
            if c >= 1:
                if willBeInfected(grid, r, c):
                    leter.append(1)
                elif grid[r-1][c] ==1 and 1 == grid[r+1][c]:
                    leter.append(1)
                else:
                    leter.append(grid[r][c])
            elif grid[r-1][c] ==1 and 1 == grid[r+1][c]:
                leter.append(1)
            else:
                leter.append(grid[r][c])
        leter.append(grid[r][columnNb-1])
        result.append(leter)
    return result

# MAIN CODE
grid = eval(input())

# Step 1 : we get the list of the cell that will be infected
newInfectedCells = getNextInfectedCells(grid) 

# Step 2 : we update the grid (cell infected will be set to 1)
# TODO  !!!!
grid = newInfectedCells
# Step 3 : print the new grid
print(grid)
            