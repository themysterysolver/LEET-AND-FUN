class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        score=0
        for i in range(k):
            largest=-heapq.heappop(heap)
            score+=largest
            largest=math.ceil(largest/3)
            heapq.heappush(heap,-largest)
        print(heap)
        return score