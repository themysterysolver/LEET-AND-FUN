"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hash=dict()
        q=deque([node])
        visited=set()
        while q:
            l=len(q)
            for i in range(l):
                n=q.popleft()
                hash[n]=Node(n.val)
                visited.add(n)
                for j in n.neighbors:
                    if j not in visited and j not in q:
                        q.append(j)
        print('printer')
        #print(hash)
        for k,v in hash.items():
            print(k.val,v.val)
        q=deque([node])
        visited=set()
        while q:
            l=len(q)
            for i in range(l):
                n=q.popleft()
                visited.add(n)
                for j in n.neighbors:
                    hash[n].neighbors.append(hash[j])
                    if j not in visited and j not in q:
                        q.append(j)
        return hash[node]
        
        



        