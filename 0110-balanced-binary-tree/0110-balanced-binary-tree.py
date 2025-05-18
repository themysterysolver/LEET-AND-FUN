# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root==None:
                return 0
            count1=check(root.left)
            count2=check(root.right)
            if count1==-1 or count2==-1 or abs(count1-count2)>1:
                return -1
            return 1+max(count1,count2)
        return check(root)!=-1
        