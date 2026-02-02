class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        def div(num):
            y = []
            while num!=0:
                y.insert(0,num%10)
                num//=10
            return y
        for num in nums:
            #print(str)
            ans.extend(div(num))
        return ans