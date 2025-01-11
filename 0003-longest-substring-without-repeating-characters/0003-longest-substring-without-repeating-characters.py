# d[s[i]] check only characters which are within the window ,which are less than the start doesn't matter!
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=dict()
        if not s:
            return 0
        if not s.strip() or len(s)==1:
            return 1
        maxi=0
        start=0
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=start: 
                start=d[s[i]]+1
            d[s[i]]=i
            maxi=max(maxi,i-start+1)
        return maxi
