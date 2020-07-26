# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #BFS
      
        queue = deque([root,])
        res = []
        level = 0
        if not root:
            return res
        while queue:
            res.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                res[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level +=1
        return res
