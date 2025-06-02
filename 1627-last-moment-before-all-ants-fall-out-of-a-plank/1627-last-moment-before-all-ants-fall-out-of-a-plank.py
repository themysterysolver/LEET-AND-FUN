class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        r=0
        l=0
        if right:
            r=n-min(right)
        if left:
            l=max(left)
        return max(l,r)
       