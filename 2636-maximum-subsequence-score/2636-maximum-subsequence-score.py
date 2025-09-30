class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        merged=sorted(zip(nums2,nums1),reverse=True)
        heap = []
        n1Sum = 0
        res = 0
        for n2,n1 in merged:
            n1Sum+=n1
            heapq.heappush(heap,n1)
            if len(heap)>k:
                p = heapq.heappop(heap)
                n1Sum-=p
            if len(heap) == k:
                res = max(res,n1Sum*n2)
        return res