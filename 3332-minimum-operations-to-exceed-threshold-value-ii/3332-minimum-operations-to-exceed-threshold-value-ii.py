class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        heapq.heapify(nums)
        while nums[0]<k:
            x,y=heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums,min(x,y)*2+max(x,y))
            count+=1
        return count
        