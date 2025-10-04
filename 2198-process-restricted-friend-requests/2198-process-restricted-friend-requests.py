#let's goo DSU
class DSU:
    def __init__(self,n):
        self.parent= [i for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        return True


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        # for u,v in restrictions:
        #     dsu.union(u,v)
        
        ans = []
        for x,y in requests:
            px,py = dsu.find(x),dsu.find(y)
            if px == py:
                ans.append(True)
                continue
            valid = True
            for r1,r2 in restrictions:
                pr1,pr2 = dsu.find(r1),dsu.find(r2)
                if px == pr1 and py == pr2 or px == pr2 and py == pr1:
                    valid = False
                    break
            if valid:
                dsu.union(x,y)
                ans.append(True)
            else:
                ans.append(False)
        return ans