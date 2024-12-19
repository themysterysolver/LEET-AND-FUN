class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=set(arr)
        k+=1
        for i in range(max(arr)+k):
            if i not in s:
                k-=1
                if k==0:
                    return i