class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result=[]
        def generate(n,s=""):
            if len(result)>len(nums):
                return
            if n==0:
                result.append(s)
                return
            generate(n-1,s+"0")
            generate(n-1,s+"1")
        generate(len(nums[0]))
        #print(result)
        sub=set(result)-set(nums)
        if sub:
            return list(sub)[0]
        else:
            return -1
        