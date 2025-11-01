class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        l,r = 0,len(palindrome)-1
        p = list(palindrome)
        flag = True
        while l<len(p):
            if p[l]!='a' and l!=len(p)//2:
                flag = False
                p[l] = 'a'
                break
            l+=1
        if flag:
            p[-1]='b'
        return ''.join(p)