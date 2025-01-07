class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                if words[i] in words[j]:
                    result.add(words[i])
        return list(result)