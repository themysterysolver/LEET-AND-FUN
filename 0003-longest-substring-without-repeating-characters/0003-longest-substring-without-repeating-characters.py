class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        idxHash=dict()
        maxi=1
        start=0
        for i in range(len(s)):
            if s[i] in idxHash and idxHash[s[i]]>=start:
                start=idxHash[s[i]]+1
            idxHash[s[i]]=i
            maxi=max(maxi,i-start+1)
        return maxi