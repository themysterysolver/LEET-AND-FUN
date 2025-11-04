class Solution:
    def findXSum(self, nums: List[int], k_: int, x: int) -> List[int]:
        c = Counter([])
        l = 0
        arr = []
        ans = []
        for i in range(len(nums)):
            arr.append(nums[i])
            l+=1
            c[nums[i]]+=1
            if l == k_:
                heap = []
                for key,val in c.items():
                    heapq.heappush(heap,(-val,-key))
                #print(heap,l)
                sumx = 0
                y = x
                while heap and y!=0:
                    v,k = heapq.heappop(heap)
                    #print(-v,-k)
                    #if -v>=x:
                    y-=1
                    sumx+=v*k
                ans.append(sumx)
                el = arr.pop(0)
                c[el]-=1
                l-=1
            #print('idx',l)
        return ans
