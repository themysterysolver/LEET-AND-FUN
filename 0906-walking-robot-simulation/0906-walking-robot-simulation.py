class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        point=[0,0]
        prevpoint=[0,0]
        current=0
        maxi=0
        obstacles=set(map(tuple,obstacles))
        for i in commands:
            if i==-1:
                current=(current+1)%4
                continue
            if i==-2:
                current=(current+3)%4
                continue
            for j in range(i):
                newx=point[0]+directions[current][0]
                newy=point[1]+directions[current][1]
                if (newx,newy) in obstacles:
                    break
                point[0],point[1]=newx,newy
            print(i,point)
            maxi=max(maxi,(point[0]**2+point[1]**2))
        return maxi
            