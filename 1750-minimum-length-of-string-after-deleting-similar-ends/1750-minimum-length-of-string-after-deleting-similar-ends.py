class Solution:
    def minimumLength(self, s: str) -> int:
        left,right = 0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                break
            while s[left] == s[right] and right-1!=left and s[left] == s[right-1]:
                right-=1
            while s[left] == s[right] and right!=left+1 and s[left+1] == s[right]:
                left+=1
            #print(s[left:right+1])
            left+=1
            right-=1
        return right-left+1
            