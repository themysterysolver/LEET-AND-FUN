class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s=columnTitle[::-1]
        num=0
        for i in range(len(s)):
            num=num+(26**i)*(ord(s[i])-ord('A')+1)
        return num