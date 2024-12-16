class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3==0:
            n=num//3
            return [n-1,n,n+1]
        else:
            return []