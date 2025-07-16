class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px, py = self.find(x) ,self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        dsu = DSU(len(s))
        for u,v in pairs:
            dsu.union(u,v)
        
        components = defaultdict(list)

        for i in range(len(s)):
            components[dsu.find(i)].append(i)
        
        result = ['']*len(s)

        for comp in components.values():
            chars = [s[i] for i in comp]
            chars.sort()
            comp.sort()
            for c,idx in zip(chars,comp):
                result[idx] = c
        
        return ''.join(result)