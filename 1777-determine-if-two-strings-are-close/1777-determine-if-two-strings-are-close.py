class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Hash=[0]*26
        word2Hash=[0]*26
        for c in word1:
            word1Hash[ord(c)-97]+=1
        for c in word2:
            word2Hash[ord(c)-97]+=1
        print(word1Hash)
        print(word1Hash)
        for i in range(26):
            if (word1Hash[i]==0 and word2Hash[i]!=0) or (word1Hash[i]!=0 and word2Hash[i]==0) :
                return False
        word1Hash.sort()
        word2Hash.sort()
        for i in range(26):
            if word1Hash[i]!=word2Hash[i]:
                return False
        return True

        