# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxi=0
        q=deque([(root,0)])
        while q:
            l=len(q)
            nodes=[]
            for i in range(l):
                r,c=q.popleft()
                nodes.append(c)
                if r.left:
                    q.append((r.left,2*c+1))
                if r.right:
                    q.append((r.right,2*c+2))
            maxi=max(maxi,max(nodes)-min(nodes)+1)
        return maxi              
