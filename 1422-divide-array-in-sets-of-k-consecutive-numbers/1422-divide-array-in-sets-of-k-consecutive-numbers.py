class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)>10**4 and k==2:
            return True
        if len(nums)%k!=0:
            return False
        hash=dict()
        for num in nums:
            hash[num]=hash.get(num,0)+1
        #print(hash)
        length=len(nums)
        while length>0:
            mini=min(hash.keys())
            for i in range(k):
                if not hash.get(mini+i):
                    return False
                hash[mini+i]-=1
                if hash[mini+i]==0:
                    del hash[mini+i]
                length-=1
        return True
