class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #instructions = instructions*3
        initital = (0,0)
        #s = set()
        #s.add((0,0))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        idx = 0
        curr = (0,0)
        for c in instructions:
            dx,dy = curr
            if c == "G":
                x,y = directions[idx]
                curr = (x+dx,y+dy)
            elif c == "L":
                idx = (idx-1)%4
            else:
                idx = (idx+1)%4
        return curr == (0,0) or idx != 0 