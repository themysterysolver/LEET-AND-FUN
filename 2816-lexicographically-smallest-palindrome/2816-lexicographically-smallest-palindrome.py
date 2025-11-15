class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = len(s)
        s = list(s)
        left = l//2-1
        right = l//2 if l%2 == 0 else l//2+1
        while left>=0:
            if s[left]<s[right]:
                s[right] = s[left]
            else:
                s[left] = s[right]
            left-=1
            right+=1
        return ''.join(s)
