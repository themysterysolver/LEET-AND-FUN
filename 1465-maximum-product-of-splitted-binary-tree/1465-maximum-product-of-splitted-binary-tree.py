# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def findTotal(root):
            if not root:
                return 0
            return findTotal(root.left)+root.val+findTotal(root.right)
        maxi = float('-inf')
        def maxProd(root):
            nonlocal maxi
            if not root:
                return 0
            sumx = maxProd(root.left)+root.val+maxProd(root.right)
            maxi = max(maxi,(sumx)*(totalSum-sumx))
            return sumx
        totalSum = findTotal(root)
        maxProd(root)
        #print(totalSum)
        return maxi%(10**9+7)