class Solution:
    def countCollisions(self,s: str) -> int:
        count=0
        while s and s[0]=="L":
            s=s[1:]
        while s and s[-1]=="R":
            s=s[:-1]
    
        return s.count("L")+s.count("R")