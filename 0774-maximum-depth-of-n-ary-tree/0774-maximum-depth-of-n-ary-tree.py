"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q=deque([root])
        depth=0
        while q:
            l=len(q)
            for _ in range(l):
                r=q.popleft()
                for n in r.children:
                    q.append(n)
            depth+=1
        return depth