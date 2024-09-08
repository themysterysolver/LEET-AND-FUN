class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir=[[1,0],[0,1],[-1,0],[0,-1]]
        cur=[0,0]
        d={'L':1,'R':3,'U':0,'D':2}
        for i in moves:
            cur[0]+=dir[d[i]][0]
            cur[1]+=dir[d[i]][1]
        if cur==[0,0]:
            return True
        else:
            return False