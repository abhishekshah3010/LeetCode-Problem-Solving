# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
#         if root is None:
#             return 0
        
#         queue = [root]
#         depth = 0
        
#         while queue:
#             depth += 1
#             for i in range(len(queue)):
#                 current_root = queue.pop(0)
#                 if current_root.left:
#                     queue.append(current_root.left)
#                 if current_root.right:
#                     queue.append(current_root.right)
#         return depth
        
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
