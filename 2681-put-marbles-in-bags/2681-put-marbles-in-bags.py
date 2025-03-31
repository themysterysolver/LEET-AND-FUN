class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        sumi=[weights[i]+weights[i+1] for i in range(n-1)]

        #print(sumi)
        sumi.sort()
        #print(sumi,sumi[n-k:n],sumi[:k-1])
        return sum(sumi[n-k:n])-sum(sumi[:k-1])