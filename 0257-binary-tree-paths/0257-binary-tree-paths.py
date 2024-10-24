# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        def dfs(root,path):
            if not root:
                return
            path+=str(root.val)
            if not root.left and not root.right:
                result.append(path)
            dfs(root.left,path+'->')
            dfs(root.right,path+'->')
        dfs(root,"")
        return result
            

        