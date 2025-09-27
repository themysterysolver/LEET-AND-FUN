# XOR ^
# think 1st index as nums and 2nd on as K
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0
# CONCEPT OF DIFFERECNE ARRAY here
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = [0]*(len(nums)+1)
        curr = 0
        count = 0
        for i in range(len(nums)):
            curr^=flips[i] #ends effect
            #then we need to flip here Coz curr = 1(flip happpened here) and nums[i] = 1 (this is curerently 0),else 0,0 flip didn't happend and nums didn't has already zero thus we need a flip here.
            #if we have 1,0 or o,1 then then flip happened on zero or no flip on 1...so this is brilliant.
            if nums[i]^curr == 0: 
                count+=1
                if i+k>len(nums):
                    return -1
                flips[i+k] = 1
                curr^=1 #ongoing
        return count


