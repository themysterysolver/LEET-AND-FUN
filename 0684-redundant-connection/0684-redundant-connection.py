class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px, py = self.find(x) ,self.find(y)
        if px==py:
            return False
        self.parent[px] = py
        return True

class Solution:
    def findRedundantConnection(self, edges):
        
        dsu = DSU(len(edges))
        for u,v in edges:
            if not dsu.union(u-1,v-1):
                return [u,v]
