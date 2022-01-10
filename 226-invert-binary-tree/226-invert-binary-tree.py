# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left
            
        dfs(root)
        return root
#         if not root:
#             return None
                
#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         temp = root.left 
#         root.left = root.right
#         root.right = temp
#         return root
        