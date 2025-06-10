class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        #print(c)
        maxi,mini=float('-inf'),float('inf')
        for key,val in c.items():
            if val&1==1:
                maxi=max(maxi,val)
            else:
                mini=min(mini,val)
        return maxi-mini