# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root,result):
            if root:
                inorder(root.left,result)
                result.append(root.val)
                inorder(root.right,result)
        result=[]
        inorder(root,result)
        for i in range(len(result)):
            if i>0:
                if result[i]<=result[i-1]:
                    return False
        return True

    