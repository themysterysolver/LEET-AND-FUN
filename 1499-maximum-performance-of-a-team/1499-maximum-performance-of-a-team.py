class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        merged=sorted(zip(efficiency,speed),reverse=True)
        heap = []
        n1Sum = 0
        res = 0
        MOD = 10**9+7
        for n2,n1 in merged:
            n1Sum+=n1
            heapq.heappush(heap,n1)
            if len(heap)>k:
                p = heapq.heappop(heap)
                n1Sum-=p
                # n1Sum%=10**9
            res = max(res,(n1Sum*n2))
        return res%MOD