# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        #0-FALSE 1-TRUE
        #2-OR 3-AND
        def postorder(root):
            if not root:
                return False
            if root.val == 0:
                return False
            if root.val == 1:
                return True
            left_val=postorder(root.left)
            right_val=postorder(root.right)
            if root.val == 2:
                return left_val or right_val
            if root.val == 3:
                return left_val and right_val
        return postorder(root)