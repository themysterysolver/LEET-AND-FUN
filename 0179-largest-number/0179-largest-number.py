class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        print (nums)
        new_list=list(map(str,nums))
        print(new_list)
        new_list.sort(key=lambda x:str(x),reverse=True)
        print(new_list)
        return ''.join(new_list)