class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        print(heap)
        while heap and len(heap)!=1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if y==x:
                continue
            heapq.heappush(heap,-(y-x))
        return -heapq.heappop(heap) if heap else 0
