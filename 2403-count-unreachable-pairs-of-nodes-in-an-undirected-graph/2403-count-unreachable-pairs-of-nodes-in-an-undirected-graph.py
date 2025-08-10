class dsu:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x) ,self.find(y)
        self.parent[px] = py
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        DSU = dsu(n)
        for u,v in edges:
            DSU.union(u,v)
        
        parent = defaultdict(int)

        for i in range(n):
            parent[DSU.find(i)] += 1
        
        total = 0
        total_nodes = n
        for size in parent.values():
            total += size * (total_nodes - size)
        return total // 2