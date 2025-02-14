# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi=float('-inf')
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root,left,count):
            if root:
                self.maxi=max(self.maxi,count)
                if left:
                    dfs(root.right,False,count+1)
                    dfs(root.left,True,1)
                else:
                    dfs(root.left,True,count+1)
                    dfs(root.right,False,1)
        dfs(root,False,0)
        return self.maxi