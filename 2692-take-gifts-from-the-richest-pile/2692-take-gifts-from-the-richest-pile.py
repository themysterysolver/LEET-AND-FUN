class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        for i in gifts:
            heapq.heappush(heap,-i)
        #print(heap)
        for i in range(k):
            g=-heapq.heappop(heap)
            g=(g**(1/2))//1
            heapq.heappush(heap,-g)
            #print(i,heap)
        #print(heap)
        heap=[-1*int(i) for i in heap]
        return sum(heap)