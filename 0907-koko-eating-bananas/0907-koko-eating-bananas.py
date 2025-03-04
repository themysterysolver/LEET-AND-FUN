class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            cost=sum([math.ceil(i/mid) for i in piles])
            if cost<=h:
                high=mid-1
            else:
                low=mid+1
        return low

