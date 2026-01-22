class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if sorted(nums)==nums:
            print('re 0')
            return 0
        arr=nums[:]
        count = 0
        while arr!=sorted(arr):
            idx = 0
            pairs = []
            for i in range(len(arr)-1):
                pairs.append((arr[i]+arr[i+1],i))
            _,idx = sorted(pairs,key=lambda x:(x[0],x[1]))[0]
            #print('pairs',sorted(pairs,key=lambda x:(x[0],x[1])),idx)
            na = [ ]
            for i in range(len(arr)):
                if i == idx:
                    na.append(arr[i]+arr[i+1])
                elif idx+1 == i:
                    continue
                else:
                    na.append(arr[i])
            #print('na',na)
            arr = na[:]
            count+=1
        return count
            
            