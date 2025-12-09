class Solution:
    def greatestLetter(self, s: str) -> str:
        lower,upper = set(),set()
        for c in s:
            if c.islower():
                lower.add(c)
            else:
                upper.add(c)
        ans = ""
        for c in sorted(''.join(upper),reverse=True):
            if chr(ord(c)+32) in lower:
                return c
        return ans
            