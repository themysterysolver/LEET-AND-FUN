# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path=[]
        def dfs(root,string):
            if root:
                string=chr(ord('a')+root.val)+string
                if not root.left and not root.right:
                    path.append(string)
                dfs(root.left,string)
                dfs(root.right,string)
        dfs(root,"")    
        path.sort()
        return path[0] if path else ""