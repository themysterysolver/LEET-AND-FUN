class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums=nums1+nums2
        hash=dict()
        result=0
        for num in nums1:
            hash[num]=hash.get(num,0)+len(nums2)
        for num in nums2:
            hash[num]=hash.get(num,0)+len(nums1)
        for key,val in hash.items():
            if val%2==1:
                result^=key
        return result