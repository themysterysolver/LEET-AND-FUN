# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result=[]
        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        inorder(root)
        mini=result[-1]-result[0]
        for i in range(1,len(result)):
            mini=min(mini,result[i]-result[i-1])
        return mini