class Solution:
    def reorganizeString(self, s: str) -> str:
        hash_freq=dict()
        for c in s:
            hash_freq[c]=hash_freq.get(c,0)+1
        #print(hash_freq)
        max_heap=[(-val,key) for key,val in hash_freq.items()]
        #print(max_heap)
        heapq.heapify(max_heap)
        #print(max_heap)
        result=""
        while len(max_heap)>1:
            f1,char1=heapq.heappop(max_heap)
            f2,char2=heapq.heappop(max_heap)
            result+=char1+char2
            if f1+1<0: 
                heapq.heappush(max_heap,(f1+1,char1)) 
            if f2+1<0:
                heapq.heappush(max_heap,(f2+1,char2)) 
            print(result)
        if max_heap:
            if -max_heap[0][0]>1:
                return ""
            result+=max_heap[0][1] 
        return result