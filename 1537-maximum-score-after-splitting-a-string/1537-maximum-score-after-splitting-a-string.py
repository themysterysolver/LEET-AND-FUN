class Solution:
    def maxScore(self, s: str) -> int:
        maxi=float('-inf')
        s=list(s)
        for i in range(len(s)-1):
            maxi=max(s[:i+1].count('0')+s[i+1:].count('1'),maxi)
            print(i,maxi)
        return maxi
# 