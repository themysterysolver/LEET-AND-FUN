class DSU:
    def __init__(self,n):
        self.parent={i:i for i in range(1,n+1)}   
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adL = defaultdict(list)
        for u,v in dislikes:
            adL[u].append(v)
            adL[v].append(u)
        
        dsu=DSU(n)
        for u in adL.keys():
            for v in adL[u]:
                if dsu.find(u)==dsu.find(v):
                    return False
                dsu.union(adL[u][0],v)
        return True