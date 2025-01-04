class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters=set(s)
        count=0
        for letter in letters:
            start,end=s.index(letter),s.rindex(letter)
            buffer=set()
            for i in range(start+1,end):
                buffer.add(s[i])
            count+=len(buffer)
        return count