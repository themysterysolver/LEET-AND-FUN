class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums)!=1:
            arr = []
            flag = True
            #print(nums,len(nums))
            l = len(nums)
            for i in range(0,l,2):
                #print(i)
                if flag:
                    arr.append(min(nums[i],nums[i+1]))
                else:
                    arr.append(max(nums[i],nums[i+1]))
                flag = not flag
            #print(arr)
            #print('-----------')
            nums = arr[:]
        return nums[0]