class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        hash={0:[],1:[]}
        for i in nums:
            hash[i%2].append(i)
        return hash[0]+hash[1]
            