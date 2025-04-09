class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        def check(arr):
            return len(arr)!=len(set(arr))
        for i in range(0,len(nums),3):
            if check(nums[i:]):
                count+=1
            else:
                break
            #print(count,check(nums[i:]),nums[i:])
        return count

