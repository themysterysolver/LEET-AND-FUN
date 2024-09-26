class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        ans=[]
        result=[]
        for i in set1:
            if i not in set2:
                result.append(i)
        ans.append(result)
        result=[]
        for i in set2:
            if i not in set1:
                result.append(i)
        ans.append(result)
        return ans