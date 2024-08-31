# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count=1
        if root==None:
            return 0
        count1=count+self.maxDepth(root.left)
        count2=count+self.maxDepth(root.right)
        return max(count1,count2)
        