# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        preorder=[]
        def pre(root):
            if root:
                pre(root.left)
                preorder.append(root.val)
                pre(root.right)
        pre(root)
        return len(set(preorder))==1