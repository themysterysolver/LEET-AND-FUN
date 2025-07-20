# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,r,res):
        if not r:
            res.append(None)
            return 
        res.append(r.val)
        self.helper(r.left,res)
        self.helper(r.right,res)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1,res2=[],[]
        self.helper(p,res1)
        self.helper(q,res2)
        print(res1,res2)
        if res1==res2:
            return True
        else:
            return False
