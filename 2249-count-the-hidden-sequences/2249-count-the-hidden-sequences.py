class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mini=0
        maxi=0
        curr=0
        for d in differences:
            curr+=d
            maxi=max(curr,maxi)
            mini=min(curr,mini)
        high,low=upper-maxi,lower-mini
        return max(0,high-low+1)