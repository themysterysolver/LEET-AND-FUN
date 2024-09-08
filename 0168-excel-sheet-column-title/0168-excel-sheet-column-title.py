class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        s=""
        while n:
            print (s)
            n-=1
            s=s+(chr(n%26+ord('A')))
            n=n//26
        return s[::-1]