class Solution:
    def maxFreqSum(self, s: str) -> int:
        if s=="":
            return 0
        c=Counter(s)
        maxiC=0
        maxiV=0
        vowel="aeiou"
        for key,val in c.items():
            if key in vowel:
                maxiV=max(maxiV,val)
            else:
                maxiC=max(maxiC,val)
        return maxiC+maxiV