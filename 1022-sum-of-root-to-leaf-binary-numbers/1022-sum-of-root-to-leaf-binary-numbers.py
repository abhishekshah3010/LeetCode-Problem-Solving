# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumRootToLeaf(root, sum):
            if root == None: 
                return 0
            sum = (2 * sum) + root.val
            if root.left == None and root.right == None: 
                return sum
            return sumRootToLeaf(root.left, sum) + sumRootToLeaf(root.right, sum)
        
        return sumRootToLeaf(root, 0)
            
        