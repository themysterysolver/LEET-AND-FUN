# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         nums = [0]*(m+n)
#         i = j = k = 0
#         while i<m and j<n:
#             if nums1[i]<nums2[j]:
#                 nums[k] = nums1[i]
#                 i += 1
#             else:
#                 nums[k] = nums2[j]
#                 j += 1
#             k += 1
#         while i<m:
#             nums[k] = nums1[i]
#             i += 1
#             k+=1
#         while j<n:
#             nums[k] = nums2[j]
#             j+=1
#             k+=1
#         return nums

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #keeping largest element at the last
        i,j,k = m-1,n-1,(m+n)-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k-=1
        return nums1
        

        