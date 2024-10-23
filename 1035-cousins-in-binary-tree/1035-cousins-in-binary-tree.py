# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def BFS(root,x,y):
            q=deque([(root,None)])
            while q:
                l=len(q)
                ans=[]
                for _ in range(l):
                    r,p=q.popleft()
                    if r.val==x:
                        if p:
                            ans.append(p.val)
                    if r.val==y:
                        if p:
                            ans.append(p.val)
                    if r.left:
                        q.append((r.left,r))
                    if r.right:
                        q.append((r.right,r))
                if len(set(ans))==2:
                    return True
            return False
        return BFS(root,x,y)