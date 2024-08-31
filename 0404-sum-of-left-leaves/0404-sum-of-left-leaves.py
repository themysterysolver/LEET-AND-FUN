# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def calci(root,isleft):
            if not root:
                return 0
            if not root.right and not root.left and isleft:
                return root.val
            return calci(root.left,True)+calci(root.right,False)
        return calci(root,False)
        
