# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42
# keep tracking of the node as path, and node as root.


def max_path_sum(self, root):

    max_sum = float('-inf')

    def traverse(node):
        nonlocal max_sum
        if node is None:
            return 0

        left = traverse(node.left)
        right = traverse(node.right)

        r = p = node.val

        if max(left, right) > 0:
            p += max(left, right)
        if left > 0: r += left
        if right > 0: r += right
        if r > max_sum:
            max_sum = r

        return p

    traverse(root)
    return max_sum
