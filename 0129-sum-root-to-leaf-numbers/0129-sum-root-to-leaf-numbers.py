# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result=[]
        def dfs(root,sumi):
            if not root:
                return 
            sumi=sumi*10+root.val
            if not root.left and not root.right:
                result.append(sumi)
            dfs(root.left,sumi)
            dfs(root.right,sumi)
        dfs(root,0)
        print(result)
        return sum(result)