# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            s.add(root.val)
            dfs(root.right)
        dfs(root)
        return sorted(list(s))[1] if len(s)>=2 else -1