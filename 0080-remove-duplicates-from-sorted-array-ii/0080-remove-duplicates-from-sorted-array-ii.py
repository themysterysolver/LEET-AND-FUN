class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash=defaultdict(int)
        start=0
        for i in range(len(nums)):
            hash[nums[i]]+=1
            if hash[nums[i]]<=2:
                nums[start]=nums[i]
                start+=1
        return start

