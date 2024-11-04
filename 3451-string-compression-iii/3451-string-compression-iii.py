class Solution:
    def compressedString(self, nums: str) -> str:
        count=0
        s=""
        current=nums[0]
        for i in range(len(nums)):
            if nums[i]==current:
                count+=1
                if count==9:
                    s+=str(9)
                    count=0
                    s+=current
            else:
                if count!=0:
                    s+=str(count)
                    s+=current
                count=1
                current=nums[i]
            if i==len(nums)-1:
                if count!=0:
                    s+=str(count)
                    s+=current
        return s