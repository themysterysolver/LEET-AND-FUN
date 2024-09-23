class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current=(0,0)
        directions={'N':(1,0),'E':(0,1),'W':(0,-1),'S':(-1,0)}
        visited=set([(0,0)])
        for i in path:
            current=(current[0]+directions[i][0],current[1]+directions[i][1])
            if current in visited:
                return True
            visited.add(current)
        return False
