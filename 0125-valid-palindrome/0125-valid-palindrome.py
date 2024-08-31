class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isupper():
                a=a+i.lower()
            elif i.isalnum():
                a=a+i
        print (a)
        b=a[::-1]
        if a[:]==b[:]:
            return True
        else:
            return False
        