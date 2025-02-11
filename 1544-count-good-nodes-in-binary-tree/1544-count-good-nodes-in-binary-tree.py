# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,maxi):
            if not root:
                return 0
            count=0
            if root.left:
                count+=helper(root.left,max(maxi,root.val))
            if root.right:
                count+=helper(root.right,max(maxi,root.val))
            if root.val>=maxi:
                count+=1
            return count
        return helper(root,root.val)