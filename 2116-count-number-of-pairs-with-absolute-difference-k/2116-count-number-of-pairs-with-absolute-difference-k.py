class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        seen=defaultdict(int)
        for num in nums:
            count+=seen[num-k]+seen[num+k]
            seen[num]+=1
        return count
