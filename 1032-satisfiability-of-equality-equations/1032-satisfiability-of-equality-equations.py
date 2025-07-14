class DSU:
    def __init__(self):
        self.parent = [i for i in range(26)]
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px , py = self.find(x),self.find(y)
        self.parent[py] = px

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        dsu = DSU()
        for s in equations:
            start,end = s[0],s[-1]
            if "==" in s:
                dsu.union(ord(start)-ord('a'),ord(end)-ord('a'))
        for s in equations:
            start,end = s[0],s[-1]
            if "!=" in s:
                if dsu.find(ord(start)-ord('a'))==dsu.find(ord(end)-ord('a')):
                    return False
        return True