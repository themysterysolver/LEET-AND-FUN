class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        final = ""
        ans = []
        for i in range(len(nums1)):
            ans.append("1"*nums1[i]+"0"*nums0[i])
        # ans.sort(key = lambda x:(-Counter(x)["1"] if "1" in Counter(x) else 0,,Counter(x)["0"] if "0" in Counter(x) else 0))
        ans.sort(key = lambda x:(x.count('0')!=0,-x.count('1'),x.count('0')))
        #print([int(ans)])
        return int(''.join(ans),2)%(10**9+7)