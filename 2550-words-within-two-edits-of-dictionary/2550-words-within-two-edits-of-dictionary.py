class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result=[]
        l=len(queries[0])
        for w in queries:
            for word in dictionary:
                count=0
                for i in range(l):
                    if word[i]==w[i]:
                        count+=1
                if l-count<=2:
                    result.append(w)
                    break
        return result