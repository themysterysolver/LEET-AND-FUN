class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_list=[str(num) for num in nums]
        num_list.sort(key=lambda x:x*10,reverse=True)
        if num_list[0]=="0":
            return  "0"
        return ''.join(num_list)
        