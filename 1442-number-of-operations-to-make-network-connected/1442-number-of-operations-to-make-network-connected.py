class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        self.parent[px] = py
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        dsu = DSU(n)

        freeEdges = 0

        for u,v in connections:
            if dsu.find(u)!=dsu.find(v):
                dsu.union(u,v)
            else:
                freeEdges += 1
        
        print(freeEdges)

        components = set()
        
        for i in range(n):
            components.add(dsu.find(i))
        
        noOfComponents = len(components)
        #print(noOfComponents)


        if freeEdges < noOfComponents - 1:
            return -1
        return noOfComponents - 1