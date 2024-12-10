class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def hrsToMins(s):
            x,y=s.split(":")
            print(x,y)
            return int(x)*60+int(y)
        s1,e1=hrsToMins(event1[0]),hrsToMins(event1[1])
        s2,e2=hrsToMins(event2[0]),hrsToMins(event2[1])
        print(s1,e1,s2,e2)
        if s1<=s2<=e1 or s1<=e2<=e1 or s2<=s1<=e2 or s2<=e1<=e2:
            return True
        else:
            return False