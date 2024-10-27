class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies>=maxi:
                result.append(True)
            else:
                result.append(False)
        return result
