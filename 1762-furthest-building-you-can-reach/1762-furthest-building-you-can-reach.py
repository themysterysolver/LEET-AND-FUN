class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i=0
        heap=[]
        while i<len(heights)-1:
            diff=heights[i+1]-heights[i]
            if diff<0:
                i+=1
            else:
                if bricks>=diff:
                    heapq.heappush(heap,-diff)
                    bricks-=diff
                elif ladders>0:
                    if heap:
                        largest=-heap[0]
                        if largest>=diff:
                            bricks+=largest
                            heapq.heappop(heap)
                            bricks-=diff
                            heapq.heappush(heap,-diff)
                    ladders-=1
                else:
                    break
                i+=1
        return i
                
