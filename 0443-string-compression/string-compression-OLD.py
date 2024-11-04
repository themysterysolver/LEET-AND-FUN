class Solution:
    def compress(self,nums: List[str]) -> int:
        count=0
        result=[]
        current=nums[0]
        for i in range(len(nums)):
            if nums[i]==current:
                count+=1
            else:
                result.append(str(current))
                current=nums[i]
                if count>1:
                    result.extend(list(str(count)))
                count=1
            if i==len(nums)-1:
                result.append(str(current))
                current=nums[i]
                if count>1:
                    result.extend(list(str(count)))
        nums[:]=result[:]
        return len(result)
