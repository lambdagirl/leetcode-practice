# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Example 1:

# Given the following tree[3, 9, 20, null, null, 15, 7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

'''
defination:  a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
=> Brute Force: compare the depth of all possible pairs of leaves, n leaves => O(n^2)

=> max leaf depth - min leaf depth <= 1
=>DFS, use a traversal that will hit leaves as quickly as possible...
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

def isBalanced(root):
    if root is None:
        return True 
    depths = []
    nodes = []
    nodes.append((root, 0))
    while len(nodes):
        node, depth = nodes.pop()

        #case: we found a leaf
        if not node.left and not node.right:
            # we only care if it's a new depth
            if depth not in depths:
                depth.append(depth)
                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if ((len(depths)> 2)) or ((len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False
        #if not a leaf
        else:

            if node.left:
                nodes.append((node.left, depth+1))
            if node.right:
                nodes.append((node.right, depth+1))

    return True




