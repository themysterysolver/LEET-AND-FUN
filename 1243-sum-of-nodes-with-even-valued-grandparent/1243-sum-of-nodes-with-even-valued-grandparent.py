# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        sumx = 0
        q = deque([(root,TreeNode(-1),TreeNode(-1))])
        while q:
            l = len(q)
            for _ in range(l):
                node,p,gp = q.popleft()
                if gp.val%2 == 0:
                    sumx+=node.val
                if node.left:
                    q.append((node.left,node,p))
                if node.right:
                    q.append((node.right,node,p))
        return sumx 
         