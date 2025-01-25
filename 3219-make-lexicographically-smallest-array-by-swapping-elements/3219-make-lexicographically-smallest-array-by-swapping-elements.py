class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr=sorted(nums)
        #print(arr,nums)
        numToHash={i:0 for i in nums}
        count=0
        for i in range(len(arr)):
            if i==0:
                numToHash[arr[0]]=0
                continue
            diff=arr[i]-arr[i-1]
            if diff>limit:
                count+=1
            numToHash[arr[i]]=count
        #print(numToHash)
        grpToNum={i:[] for i in set(numToHash.values())}
        for num in arr:
            grpToNum[numToHash[num]].append(num)
        #print(grpToNum)
        for val in grpToNum.values():
            val.sort()
        #print(grpToNum)
        result=[]
        for i in nums:
            #print(i,result,grpToNum)
            result.append(grpToNum[numToHash[i]].pop(0))
        #print(result)
        return result
