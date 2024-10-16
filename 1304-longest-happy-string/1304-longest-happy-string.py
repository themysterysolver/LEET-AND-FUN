class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq=[]
        if a>0:
            freq.append(('a',a))
        if b>0:
            freq.append(('b',b))
        if c>0:
            freq.append(('c',c))
        max_heap=[(-val,key) for key,val in freq]
        result=""
        heapq.heapify(max_heap)
        print(max_heap)
        while max_heap:
            val1,char1=heapq.heappop(max_heap)
            if len(result)>=2 and result[-1]==char1 and result[-2]==char1:
                if not max_heap:
                    break
                val2,char2=heapq.heappop(max_heap)
                val2+=1
                result+=char2
                if val2<0:
                    heapq.heappush(max_heap,(val2,char2))
                heapq.heappush(max_heap,(val1,char1))
            else:
                val1+=1
                result+=char1
                if val1<0:
                    heapq.heappush(max_heap,(val1,char1))
        return result