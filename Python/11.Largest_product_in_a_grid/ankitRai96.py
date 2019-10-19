# Author: ankitRai96
# Problem: Find largest product in a grid

import random as r

def grid_product(grid,i,j,n):
    '''
        i: x index of element
        j: y index of element
        n: size of matrix
    '''
    # upward direction product
    if j - 3 < 0:
        up = 0
    else:
        up =  grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3]
    
    # downward direction product
    if j + 3 > n-1:
        down = 0
    else:
        down = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3] 
    
    # leftward direction product
    if i - 3 < 0:
        left = 0
    else:
        left = grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j]
    # rightward direction product
    if i + 3 > n-1:
        right = 0
    else:
       right = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
    # diagnol direction product
    if i+3 > n-1 or j+3 > n-1:
        d1 = 0
    else:
        d1 = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
    # anti-diagnol direction product
    if i-3 < 0 or j-3 < 0:
        d2 = 0
    else:
        d2 = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3] 

    return max(up,down,left,right,d1,d2)

def display_grid(grid):
    # function to display grid
    for column in grid:
        for element in column:
            print(element, end=' ')
        print()

def largest_grid_product(grid):
    largest_product = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            res = grid_product(grid,x,y,len(grid))
            if res > largest_product:
                largest_product = res
    return largest_product
if __name__ == "__main__":
    # generating radomized grid
    # 1 < element < 100 
    grid = []
    size = int(input('Enter size of grid: '))
    for _ in range(size):
        grid.append([r.randint(0,100) for _ in range(size)])
    display_grid(grid)
    print(largest_grid_product(grid))