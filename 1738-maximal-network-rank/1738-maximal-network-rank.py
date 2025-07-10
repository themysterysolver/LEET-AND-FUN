class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adL = defaultdict(list)
        hash = defaultdict(int)
        for u,v in roads:
            adL[u].append(v)
            adL[v].append(u)
            hash[u]+=1
            hash[v]+=1

        # print(hash)
        maxi = 0
        for u in range(n):
            for v in range(u+1,n):
                count = hash[u]+hash[v]
                if v in adL[u]:
                    count-=1 
                maxi = max(maxi,count)
        return maxi
        