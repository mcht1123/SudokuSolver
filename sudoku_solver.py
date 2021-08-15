
def free_square(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == -1:
                return i,j
    return None,None



def is_valid(number,grid,row,col):
    if number in grid[row]:
        return False
    for i in range(9):
        if grid[i][col] == number:
            return False

    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if grid[r][c] == number:
                return False
    return True

    


def solve(grid):

    row,col = free_square(grid)

    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(guess,grid,row,col):
            grid[row][col] = guess
            if solve(grid):
                return True
    
        grid[row][col] = -1
    
    return False

sudoku = [[-1,5,-1,    -1,-1,-1    ,-1,-1,9],
          [-1,-1,1,    -1,-1,-1,   2,-1,-1],
          [-1,4,-1,    -1,6,2,    -1,-1,-1],
          [-1,-1,-1,   -1,3,-1,   -1,1,-1],
          [-1,-1,-1,   -1,-1,-1,  9,7,8],
          [-1,-1,-1,   4,1,-1,   -1,5,-1],
          [7,-1,8,    -1,-1,1,    -1,-1,-1],
          [9,-1,-1,    7,-1,-1,    5,-1,-1],
          [-1,-1,-1,  8,-1,-1,   -1,-1,-1]]
solve(sudoku)
print(sudoku)
