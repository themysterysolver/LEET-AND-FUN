class Solution:
    def queryString(self, s: str, n: int) -> bool:
        se = set()
        for i in range(len(s)):
            for j in range(i,len(s)):
                x = int(s[i:j+1],2)
                if 1<=x<=n:
                    se.add(x)
        #print(se)
        return len(se) == n