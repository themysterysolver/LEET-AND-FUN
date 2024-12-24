class Solution:
    def validPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        while start<end:
            if s[start]!=s[end]:
                str1=s[:start]+s[start+1:]
                str2=s[:end]+s[end+1:]
                return str1==str1[::-1] or str2==str2[::-1]
            start+=1
            end-=1
        return True
        