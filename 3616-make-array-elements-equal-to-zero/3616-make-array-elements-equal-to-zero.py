class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(idx,dir):
            temp=nums.copy()
            while 0<=idx<=len(temp)-1:
                if temp[idx]==0:
                    idx+=dir
                elif temp[idx]>0:
                    temp[idx]-=1
                    dir=-dir
                    idx+=dir
            return all(x==0 for x in temp)
        valid=0
        for i in range(len(nums)):
            if nums[i]==0:
                if simulate(i,-1):
                    valid+=1
                if simulate(i,1):
                    valid+=1
        return valid