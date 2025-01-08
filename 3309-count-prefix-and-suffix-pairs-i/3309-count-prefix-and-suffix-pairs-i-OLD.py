class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            str1=words[i]
            for j in range(i+1,len(words)):
                str2=words[j]
                if str1==str2[:len(str1)] and str1==str2[len(str2)-len(str1):]:
                    count+=1
        return count
