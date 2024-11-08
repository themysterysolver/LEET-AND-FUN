class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        totalXOR=[0]*len(nums)
        totalXOR[0]=nums[0]
        answer=[]
        for i in range(1,len(nums)):
            totalXOR[i]=totalXOR[i-1] ^ nums[i]
        mask=(1<<maximumBit)-1
        for i in range(len(totalXOR)-1,-1,-1):
            answer.append(totalXOR[i] ^ mask)
        return answer

        
        
        
            

