
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

#2^(m+n) Time complexity
def minPathSum(grid):
    #boundry case
    def caculate_grid(grid, row, col):
        #edge case
        if row == len(grid) or col == len(grid[0]):
            return float('inf')
        #when in the right bottom
        if row == len(grid) -1 and col == len(grid) -1:
            return grid[row][col]
        return grid[row][col] + min(caculate_grid(grid,row+1,col),caculate_grid(grid,row,col+1))
    return caculate_grid(grid,0,0)


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))
