class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        l =len(arr)
        prefix = [float('-inf')] * l
        suffix = [float('-inf')] * l

        prefix[0] = arr[0]
        suffix[-1] = arr[-1]

        for i in range(1,l):
            prefix[i] = max(arr[i],prefix[i-1]+arr[i])
        for i in range(l-2,-1,-1):
            suffix[i] = max(suffix[i+1]+arr[i],arr[i])
        
        maxi = max(prefix)
        for i in range(1,l-1):
            maxi = max(maxi, prefix[i-1]+suffix[i+1])
        return maxi