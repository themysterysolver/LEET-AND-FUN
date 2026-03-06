class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seg = False
        for i in range(len(s)):
            if s[i]!='1' and not seg:
                seg = True
            if s[i]=='1' and seg:
                return False
        return True
            