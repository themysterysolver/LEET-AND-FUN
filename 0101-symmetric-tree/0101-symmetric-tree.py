# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,leftN,rightN):
        if leftN==None and rightN==None:
            return True
        elif leftN==None or rightN==None:
            return False
        elif leftN.val==rightN.val:
            return self.isSame(leftN.left,rightN.right) and self.isSame(leftN.right,rightN.left)
        else:
            return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.isSame(root.left,root.right)
            