# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            if root:
                #print(root)
                l,r = False,False
                if root.left:
                    l = prune(root.left)
                    if not l:
                        root.left = None
                if root.right:
                    r = prune(root.right)
                    if not r:
                        root.right = None
                if root.val == 1:
                    return True
                return l or r

            else:
                return False
        prune(root)

        return root if prune(root) else None