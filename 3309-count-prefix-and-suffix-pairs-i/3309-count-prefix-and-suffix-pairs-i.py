class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            str1=words[i]
            for j in range(i+1,len(words)):
                str2=words[j]
                if len(str1)>len(str2):
                    continue
                if str2.startswith(str1) and str2.endswith(str1):
                    count+=1
        return count