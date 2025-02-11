class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l=len(part)
        while part in s:
            idx=s.index(part)
            s=s[:idx]+s[l+idx:]
        return s