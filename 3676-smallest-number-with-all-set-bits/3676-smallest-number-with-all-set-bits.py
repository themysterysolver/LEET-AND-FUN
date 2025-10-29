class Solution:
    def smallestNumber(self, n: int) -> int:
        nums =(bin(n)[2:])
        print(len(nums),nums)
        return int("1"*len(nums),2)