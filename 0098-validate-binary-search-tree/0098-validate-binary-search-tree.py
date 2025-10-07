# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,mini,maxi):
            if not root:
                return True
            if not (mini < root.val < maxi):
                print(root.val)
                return False
            return dfs(root.left,mini,root.val) and dfs(root.right,root.val,maxi)            
        return dfs(root,float('-inf'),float('inf'))

    