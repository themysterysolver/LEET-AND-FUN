"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def BFS(root):
            q=deque([])
            if not root:
                return root
            q.append(root)
            while q:
                l=len(q)
                ans=[]
                for i in range(l):
                    r=q.popleft()
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                    ans.append(r)
                for i in range(len(ans)):
                    if i==len(ans)-1:
                        continue
                    ans[i].next=ans[i+1]
            return root
        return BFS(root)