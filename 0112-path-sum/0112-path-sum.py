# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,sum):
            if not root:
                return 
            if sum-root.val==0 and not root.left and not root.right:
                return True
            return dfs(root.left,sum-root.val) or dfs(root.right,sum-root.val)
        return True if dfs(root,targetSum) else False