class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        l=len(nums)
        hash=Counter(nums)
        hash_left=defaultdict(int)
        for i in range(l):
            hash[nums[i]]-=1
            hash_left[nums[i]]+=1
            #print(i,list(hash_left.items()),list(hash.items()))
            if hash_left[nums[i]]*2>i+1 and hash[nums[i]]*2>l-i-1:
                return i
        return -1

        