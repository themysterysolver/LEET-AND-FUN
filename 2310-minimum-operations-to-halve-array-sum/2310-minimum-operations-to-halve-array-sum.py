class Solution:
    def halveArray(self, nums: List[int]) -> int:
        count=0
        sumi=sum(nums)
        heap=[]
        temp=sumi
        sumi/=2
        for num in nums:
            heapq.heappush(heap,-num)
        count=0
        #print(temp,sumi)
        while temp>sumi:
            t=-heapq.heappop(heap)
            #print(count,t)
            temp-=t/2
            heapq.heappush(heap,-t/2)
            #print(heap,temp,sumi)
            count+=1
        return count