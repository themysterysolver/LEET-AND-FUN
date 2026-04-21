#ins't it pretty doable?
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)
        left = {num:i for i,num in enumerate(nums1)}
        right = {num:i for i,num in enumerate(nums2)}
        s = set(nums1) & set(nums2)
        MOD = 10**9+7
        print(s,len(s))
        @cache
        def dp(idx,flag): #flag true na nums2
            #print(idx1,idx2,flag)
            if (not flag and idx == l1) or (flag and idx == l2):
                return 0
            #choose 2 paths either procceed further or branch?
            ans = nums2[idx] if flag else nums1[idx]
            if flag:
                choose = 0
                if nums2[idx] in s:
                    choose = dp(left[nums2[idx]] + 1,False)
                not_choose = dp(idx+1,True)
                return (max(choose,not_choose)+ans)
            else:
                choose = 0
                if nums1[idx] in s:
                    choose = dp(right[nums1[idx]] + 1,True)
                not_choose = dp(idx+1,False)
                return (max(choose,not_choose)+ans)
        return max(dp(0,True),dp(0,False))%MOD
        # return 0