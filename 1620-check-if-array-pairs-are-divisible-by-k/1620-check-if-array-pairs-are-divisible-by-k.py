class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequency=dict()
        for i in arr:
            rem=((i%k)+k)%k
            if rem in frequency:
                frequency[rem]+=1
            else:
                frequency[rem]=1
        if frequency.get(0,0)%2!=0:
            return False
        for i in range(1,k//2+1):
            if frequency.get(i,0)==frequency.get(k-i,0):
                continue
            else:
                return False
        return True
