class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sumx = 0
        for i in range(k):
            sumx+=arr[i]
        if sumx/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            sumx-=arr[i-k]
            sumx+=arr[i]
            if sumx/k>=threshold:
                count+=1
        return count    