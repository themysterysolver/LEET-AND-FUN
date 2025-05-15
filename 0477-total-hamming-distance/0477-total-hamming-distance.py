class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        score=0
        for bit in range(32):
            count=0
            for num in nums:
                #print(bit,bin(num>>bit))
                if num>>bit&1==1:
                    count+=1
            score+=(len(nums)-count)*count
        return score
            