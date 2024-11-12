class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prefixArr=[]
        maxi=nums[0]
        score=[]
        sumi=0
        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
            nums[i]+=maxi
            #prefixArr.append(nums[i])
            sumi+=nums[i]
            score.append(sumi)
            #print(i,prefixArr,score,maxi)
        return score