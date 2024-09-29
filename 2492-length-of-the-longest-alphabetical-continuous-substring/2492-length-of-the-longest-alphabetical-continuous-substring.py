class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maximum=0
        count=1
        for i in range(len(s)):
            if i==0:
                continue
            if ord(s[i])-1==ord(s[i-1]):
                print(ord(s[i])-1,ord(s[i-1]))
                count+=1
            else:
                maximum=max(maximum,count)
                count=1
        maximum=max(maximum,count)
        return maximum