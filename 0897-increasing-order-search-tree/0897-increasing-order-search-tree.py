# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        def inorder(node):
            if not node:
                return
            #print(node.val)
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        peak = TreeNode(0)
        temp = peak
        for num in result:
            temp.right = TreeNode(num)
            temp = temp.right
        return peak.right