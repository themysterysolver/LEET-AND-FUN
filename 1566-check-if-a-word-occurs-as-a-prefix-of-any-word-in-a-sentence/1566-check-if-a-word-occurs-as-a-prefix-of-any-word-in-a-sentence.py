class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split()
        print(s)
        for i in range(len(s)):
            if searchWord in s[i] and s[i].index(searchWord)==0:
                print(s[i].index(searchWord)==0)
                return i+1
        return -1