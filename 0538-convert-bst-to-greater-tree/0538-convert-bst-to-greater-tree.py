# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rcl(root,currSum):
            if root:
                rsum=rcl(root.right,currSum)
                root.val+=rsum
                return rcl(root.left,root.val)
            else:
                return currSum
        rcl(root,0)
        return root