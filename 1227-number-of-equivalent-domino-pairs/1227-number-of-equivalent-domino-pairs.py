class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for num in dominoes:
            num.sort()
        pre=list(map(tuple,dominoes))
        #print(type(pre[0]))
        hash=defaultdict(int)
        count=0
        for t in pre:
            count+=hash[t]
            hash[t]+=1
        return count