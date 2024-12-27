# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def DFS(root):
            if not root:
                return ""
            if root.right:
                return str(root.val)+"("+DFS(root.left)+")("+DFS(root.right)+")"
            if root.left:
                return str(root.val)+"("+DFS(root.left)+")"
            return str(root.val)
        return DFS(root)
