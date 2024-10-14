class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[]
        for i in piles:
            heapq.heappush(heap,-i)
        for i in range(k):
            largest=-heapq.heappop(heap)
            heapq.heappush(heap,-largest//2)
        return -sum(heap)
        