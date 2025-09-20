class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        one,two = 0,0
        res = ""
        while one<len(word1) and two<len(word2):
            if word1[one] == word2[two]:
                if word1[one:]>word2[two:]:
                    res+=word1[one]
                    one+=1
                else:
                    res+=word2[two]
                    two+=1
            else:
                if word1[one]>word2[two]:
                    res+=word1[one]
                    one+=1
                else:
                    res+=word2[two]
                    two+=1
        while one<len(word1):
            res+=word1[one]
            one+=1
        while two<len(word2):
            res+=word2[two]
            two+=1
        return res
