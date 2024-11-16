class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        result=[-1]*(len(nums)-k+1)
        counter=1#counter for consecutive_element
        #print('i,c,n,n+1')
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                counter+=1
            else:
                counter=1
            if counter>=k:
                result[i-k+2]=nums[i+1]
            #print(i,counter,nums[i],nums[i+1])
        return result
            

