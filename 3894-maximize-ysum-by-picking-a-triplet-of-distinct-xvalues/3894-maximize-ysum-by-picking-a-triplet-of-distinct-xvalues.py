class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        c=defaultdict(int)
        for i in range(len(x)):
            c[x[i]]=max(c[x[i]],y[i ])
        #print(c)
        if len(c)<3:
            return -1
        hash=list(c.items())
        hash.sort(key=lambda x:-x[1])
        #print(hash)
        sumx=0
        for i in range(3):
            sumx+=hash[i][1]
        return sumx