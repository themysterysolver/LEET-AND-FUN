class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel="aeiou"
        def isvowel(s):
            if s[0] in vowel and s[-1] in vowel:
                return 1
            return 0
        prefixsum=[0]*len(words)
        for i in range(len(words)):
            if i==0:
                prefixsum[i]=isvowel(words[i])
            else:
                prefixsum[i]=prefixsum[i-1]+isvowel(words[i])
        print(prefixsum)
        result=[0]*len(queries)
        for idx,q in enumerate(queries):
            x,y=q[0],q[1]
            x-=1
            if x==-1:
                result[idx]=prefixsum[y]
            else:
                result[idx]=prefixsum[y]-prefixsum[x]
        print(result)
        return result


            