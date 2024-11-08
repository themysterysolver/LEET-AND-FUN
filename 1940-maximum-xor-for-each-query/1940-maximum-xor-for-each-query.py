class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefixXOR=[0]*len(nums)
        prefixXOR[0]=nums[0]
        answer=[]
        for i in range(1,len(nums)):
            prefixXOR[i]=prefixXOR[i-1] ^ nums[i]
        mask=(1<<maximumBit)-1
        for i in range(len(prefixXOR)-1,-1,-1):
            answer.append(prefixXOR[i] ^ mask)
        return answer

        
        
        
            

