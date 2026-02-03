class Solution:
    def reverseByType(self, s: str) -> str:
        lr = []
        sr = []
        for c in s:
            if c.islower():
                lr.append(c)
            else:
                sr.append(c)
        ans = ""
        for c in s:
            if c.islower():
                ans+=lr.pop()
            else:
                ans+=sr.pop()
        return ans