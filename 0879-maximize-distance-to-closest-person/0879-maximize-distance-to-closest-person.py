class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l=len(seats)
        left,right=[l]*l,[l]*l
        for i in range(l):
            if seats[i]==1:
                left[i]=0
            elif i>0:
                left[i]=left[i-1]+1
        for j in range(l-1,-1,-1):
            if seats[j]==1:
                right[j]=0
            elif j<l-1:
                right[j]=right[j+1]+1
        return max(min(left[idx],right[idx]) for idx,seat in enumerate(seats) if seat==0)