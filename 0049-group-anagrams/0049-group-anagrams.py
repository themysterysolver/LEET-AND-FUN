class Solution(object):
    

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def check(i):
            di=dict()
            for a in i:
                if a not in di:
                    di[a]=1
                else:
                    di[a]=di[a]+1
            return di
        anagram=dict()
        for i in strs:
            s=tuple(sorted(check(i).items()))
            print s
            if s not in anagram:
                anagram[s]=[i]
            else:
                anagram[s].append(i)
        return list(anagram.values())