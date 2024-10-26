# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def modBFS(root):
            q=deque([root])
            result=[]
            while q:
                l=len(q)
                first=True
                for _ in range(l):
                    r=q.popleft()
                    if first:
                        first=False
                        if not r.left and not r.right:
                            result.append(r.val)
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
            print(result)
            return result
        ans=modBFS(root)
        return ans[-1]
        