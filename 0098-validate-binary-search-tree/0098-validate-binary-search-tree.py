# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateBST(root,lbound,rbound):
            if not root:
                return True
            return root.val<rbound and root.val>lbound and validateBST(root.left,lbound,root.val) and validateBST(root.right,root.val,rbound)
        return validateBST(root,float('-inf'),float('inf'))