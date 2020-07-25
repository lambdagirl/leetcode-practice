# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# A partially filled sudoku which is valid.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Example 1:

# Input:
# [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# Output: true
# Example 2:

# Input:
# [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
# modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:

# A Sudoku board(partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.

def is_unit_valid(unit):
    values = [ i for i in unit if i != '.']
    return len(set(values)) == len(values)

def is_row_valid(board):
    for row in board:
        if not is_unit_valid(row):
            return False 
    return True
        
def is_col_valid(board):
    for col in zip(*board):
        if not is_unit_valid(col):
            return False 
    return True

def is_box_valid(board):
    for i in (0,3,6):
        for j in (0,3,6):
            box = [board[x][y] for x in range(i,i+3)
                                for y in range(j,j+3)]
            if not is_unit_valid(box):
                return False
    return True

def isValidSudoku(board):
    return is_row_valid(board) and is_col_valid(board) and is_box_valid(board)
        

