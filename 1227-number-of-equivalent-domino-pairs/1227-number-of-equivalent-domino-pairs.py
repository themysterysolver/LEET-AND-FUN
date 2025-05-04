class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for num in dominoes:
            num.sort()
        pre=list(map(tuple,dominoes))
        hash=defaultdict(int)
        count=0
        for t in dominoes:
            count+=hash[tuple(t)]
            hash[tuple(t)]+=1
        return count