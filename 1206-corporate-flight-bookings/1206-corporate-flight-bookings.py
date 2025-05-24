#similar to ZERO ARRAY TRANSFORMATION-1 difference array with prefix sum
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffArray=[0]*(n+2)
        for l,r,val in bookings:
            diffArray[l]+=val
            diffArray[r+1]-=val
        booking=[0]*(n+1)
        curr=0
        for i in range(n+1):
            curr+=diffArray[i]
            booking[i]=curr
        #print(booking)
        return booking[1:]
