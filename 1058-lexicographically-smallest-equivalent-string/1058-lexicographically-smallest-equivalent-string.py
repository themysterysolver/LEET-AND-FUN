#modified DSU
class DSU:
    def __init__(self):
        self.parent = list(range(26))
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp,yp = self.find(x) , self.find(y)
        if xp==yp:
            return
        if xp<yp:
            self.parent[yp] = xp
        else:
            self.parent[xp] = yp
    


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        dsu = DSU()
        for x,y in zip(s1,s2):
            dsu.union(ord(x)-ord('a'),ord(y)-ord('a'))
        
        result = []
        for c in baseStr:
            smallChar = dsu.find(ord(c)-ord('a'))
            result.append(chr(smallChar+ord('a')))
        
        return ''.join(result)
