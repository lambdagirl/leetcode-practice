# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.

# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

# Example 1:

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0
# Example 2:

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
# Example 3:

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

# Constraints:

# 1 <= arr.length <= 5000
# 0 <= arr[i] <= 9
# Each node's value is between [0 - 9].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        return self.helper(root, arr, 0)

    def isLeaf(self, node: TreeNode):
        if node is None:
            return False
        return node.left is None and node.right is None

    def helper(self, root: TreeNode, arr: List[int], i: int) -> bool:
        if root is None or i == len(arr):
            return False

        if root.val != arr[i]:
            return False

        if self.isLeaf(root) and i == len(arr) - 1:  # is leaf node
            return True

        return self.helper(root.left, arr, i + 1) or self.helper(
            root.right, arr, i + 1)


def isValidSequence2(self, root: TreeNode, arr: List[int]) -> bool:
    if not arr or not root:
        return False
    # if our root value doesn't match, there is no reason to move forward
    if root.val != arr[0]:
        return False

    # if we reach the leaf node and there is only 1 element left in the array, we should return True
    if not root.left and not root.right and len(arr) == 1:
        return True

    left = self.isValidSequence(root.left, arr[1:])
    # checking right child
    right = self.isValidSequence(root.right, arr[1:])
    return left or right
