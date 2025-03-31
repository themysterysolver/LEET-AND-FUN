class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start=0
        end=k
        nums=[(-num,idx) for idx,num in enumerate(nums)]
        print("NUMS-EN",nums)
        result=[]
        heap=nums[start:end]
        print("HEAP",heap)
        heapq.heapify(heap)
        x,y=heap[0]
        result.append(-1*x)
        for i in range(k,len(nums)):
            value,index=nums[i]
            heapq.heappush(heap,(value,index))
            start+=1
            end+=1
            while True:
                val,idx=heap[0]
                if idx<start:
                    heapq.heappop(heap)
                    continue
                else:
                    result.append(-1*val)
                    break
        return result


