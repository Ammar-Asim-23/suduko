#Create a 2D list to represent the Sudoku grid, with all elements initially set to 0.
grid = [[0 for x in range(9)] for y in range(9)]
#Implement a function to print the grid in a formatted way
def print_grid(grid):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")
'''Implement a function to check if the entered number is valid in the current position,
it should check if the number is not already in the current row, current column and current 3x3 subgrid'''
def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol] == num:
                return False
    return True
#Implement a function to solve the sudoku using backtracking algorithm
def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1,10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        else:
                            grid[row][col] = 0
                return False
    return True
#Now you can run the solve function on the grid, and it will fill in the empty cells with the correct numbers.
solve(grid)
print_grid(grid)
