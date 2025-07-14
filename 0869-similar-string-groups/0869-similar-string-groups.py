class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px, py = self.find(x),self.find(y)
        self.parent[px] = py
 
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        l = len(strs[0])
        def is_similar(x,y):
            diff = 0
            for i in range(l):
                if x[i]!=y[i]:
                    diff+=1
            return diff<=2
        
        dsu = DSU(len(strs))

        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if is_similar(strs[i],strs[j]):
                    dsu.union(i,j)

        
        parents = set()
        for u in range(len(strs)):
            parents.add(dsu.find(u))
        
        return len(parents)
