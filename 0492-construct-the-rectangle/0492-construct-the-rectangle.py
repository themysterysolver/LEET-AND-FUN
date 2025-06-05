class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        result=[]
        for num in range(area,0,-1):
            if area%num==0:
                l,w=num,area//num
                if l>=w:
                    result.append((l-w,[l,w]))
        heapq.heapify(result)
        #print(result)
        _,ans=heapq.heappop(result)
        #ans=0
        return ans
