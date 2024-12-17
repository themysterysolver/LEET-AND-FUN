class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap=[(-ord(key),val) for key,val in Counter(s).items()]
        print(heap)
        heapq.heapify(heap)
        print(heap)
        result=""
        while heap:
            c,val=heapq.heappop(heap)
            c=chr(-c)
            result+=c*min(val,repeatLimit)
            if val>repeatLimit and heap:
                c1,val1=heapq.heappop(heap)
                result+=chr(-c1)
                if val1>1:
                    heapq.heappush(heap,(c1,val1-1))
                heapq.heappush(heap,(-ord(c),val-min(val,repeatLimit)))
        return result
