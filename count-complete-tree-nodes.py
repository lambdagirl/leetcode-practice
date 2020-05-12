# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6

# Approach 1:Linear Time | recursion


class TreeNode:
    def __init__(self, val=0, left=None, right=None)
    self.val = val
    self.left = left
    self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)
# Approach 2:Binary Search


# 1. Return 0 if the tree is empty.

# Compute the tree depth d.

def getDepth(self, root: TreeNode) -> int:
    """Return tree depth in O(d) time."""
    if not root:
        return 0
    return 1 + self.getDepth(root.left)


def countNodes(self, root: TreeNode) -> int:
    if not root:
        return 0
    leftDepth = self.getDepth(root.left)
    rightDepth = self.getDepth(root.right)
    if leftDepth == rightDepth:
        return pow(2, leftDepth) + self.countNodes(root.right)
    else:
        return pow(2, rightDepth) + self.countNodes(root.left)
