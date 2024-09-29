class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                #print(i,j,k)
                if nums[i]+nums[j]+nums[k]==0:
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    continue
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
            #print(result)
            #print('-------------------------')
        return result

            