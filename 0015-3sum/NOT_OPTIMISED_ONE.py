class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result=[]
        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            while j<k:
                #print(i,j,k)
                if nums[i]+nums[j]+nums[k]==0:
                    if [nums[i],nums[j],nums[k]] in result:
                        j+=1
                        k-=1
                        continue
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

            
