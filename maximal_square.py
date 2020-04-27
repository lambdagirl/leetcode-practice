# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4


def maximalSquare(matrix):
    max_len = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = int(matrix[r][c])
            if matrix[r][c] and r > 0 and c > 0:
                matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1],
                                   matrix[r - 1][c - 1]) + 1
            if matrix[r][c] > max_len:
                max_len = matrix[r][c]
    return max_len * max_len


test = maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                      ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
print(test)