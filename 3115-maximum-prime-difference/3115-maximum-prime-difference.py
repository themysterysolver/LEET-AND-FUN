class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        maxi = max(nums)
        is_prime = [True]*(maxi+1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2,int(math.sqrt(maxi))+1):
            if is_prime[i]:
                for j in range(i*i,maxi+1,i):
                    is_prime[j] = False
        
        #print(is_prime)
        l,r = -1,-1
        for i,num in enumerate(nums):
            if is_prime[num]:
                l = i
                break
        for j in range(len(nums)-1,-1,-1):
            if is_prime[nums[j]]:
                r = j
                break
        #print(nums,l,r)
        return r-l


