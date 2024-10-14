class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        print(nums)
        for i in range(k-1): 
            heapq.heappop(nums)
        return -heapq.heappop(nums)
