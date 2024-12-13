class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        heap=[]
        visited=set()
        for i,x in enumerate(nums):
            heapq.heappush(heap,(x,i))
        #print(heap)
        while heap:
            s,idx=heapq.heappop(heap)
            if idx not in visited:
                visited.add(idx+1)
                visited.add(idx-1)
                score+=s
            #print(score,idx,s,visited)
        return score
