class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f=Counter(nums2)
        result=[]
        for i in nums1:
            if i in f:
                f[i]-=1
                result.append(i)
                if f[i]==0:
                    del f[i]
        return result