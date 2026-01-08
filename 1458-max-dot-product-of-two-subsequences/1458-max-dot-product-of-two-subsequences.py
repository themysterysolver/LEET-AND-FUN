class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)
        @cache
        def go(idx1,idx2):
            if idx1>=l1 or idx2>=l2:
                return float('-inf')
            pick = nums1[idx1]*nums2[idx2]+max(0,go(idx1+1,idx2+1))
            skip = max(go(idx1+1,idx2),go(idx1,idx2+1))
            return max(skip,pick)
        return go(0,0)